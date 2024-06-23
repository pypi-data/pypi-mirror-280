import re
import datetime
from urllib.parse import urlparse
from django.conf import settings
from django.utils import timezone
from django.utils.crypto import get_random_string
from .models import ShortenedURL
import logging
logger = logging.getLogger("normal")

ALIAS_REGEX = re.compile("^[a-zA-Z0-9]+$")
MAX_ALIAS_LENGTH = 15

def get_current_dtm():
    try:
        return timezone.localtime(timezone.now())
    except:
        return datetime.datetime.now()
    
def validate_url(url):
    url_pattern = re.compile(r'^(https?)://[A-Za-z0-9.-]+(\:[0-9]+)?/?.*$')

    if not url_pattern.match(url):
        return False
    return True

def parse_url(url):
    logger.debug("parse_url parsing url")
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        logger.error(f"parse_url no scheme in parsed url")
        url = f'https://{url}'
        return parse_url(url)
    
    if not parsed_url.netloc or not parsed_url.path:
        logger.error(f"parse_url no netloc or path in parsed url")
        return 0, 'Invalid URL', None
    
    logger.debug(f"parse_url validating url {url}")
    check_url = validate_url(url)
    if not check_url:
        logger.error("parse_url invalid url")
        return 0, 'Invalid URL', None

    url = parsed_url.geturl()
    return 1, '', urlparse(url)

def is_alias_valid(alias):
    result = ALIAS_REGEX.search(alias)
    if not result:
        return 0, 'Alias format is not valid'
    if result.end() > MAX_ALIAS_LENGTH:
        return 0, f'Maximum alias length allowed is {MAX_ALIAS_LENGTH}'

    return 1, ''

def get_base_data(post_data):
    status, message, parsed_url = parse_url(post_data['original_url'])
    if not status:
        logger.error(f"get_base_data {message}")
        return 0, message, None
    
    logger.debug("get_base_data appending data in response")
    post_data['original_url'] = parsed_url.geturl()
    post_data["base_scheme"] = parsed_url.scheme
    post_data["base_domain"] = parsed_url.netloc
    post_data['url'] = parsed_url.path
    post_data['expires_at'] = timezone.now() + datetime.timedelta(int(settings.URLSHORT['EXPIRES_AT']))
    if parsed_url.params:
        post_data['url'] += f';{parsed_url.params}'
    if parsed_url.query:
        post_data['url'] += f'?{parsed_url.query}'
    if parsed_url.fragment:
        post_data['url'] += f'#{parsed_url.fragment}'
    if not post_data.get('scheme'):
        post_data['scheme'] = settings.URLSHORT['URLSHORT_SCHEME']
    if not post_data.get('domain'):
        post_data['domain'] = settings.URLSHORT['URLSHORT_DOMAIN']
    if post_data.get('alias'):
        status, message = is_alias_valid(post_data.get('alias'))
        if not status:
            return status, message, None
    
    logger.debug(f"get_base_data returning response")
    return 1, '', post_data


def generate_short_url(data):
    current_timestamp = timezone.now()
    url = data.get("original_url")
    alias = data.get('alias')
    logger.debug(f"generate_short_url checking if url already exist with alias {alias}")
    if alias and ShortenedURL.objects.filter(
        unique_id=alias,
        expires_at__gt=current_timestamp,
        base_scheme=data.get('base_scheme'),
        base_domain=data.get('base_domain'),
        is_active=True
    ).exists():
        failure_reason = f"Record with {alias} and {url} already exists"
        logger.debug(failure_reason)
        return {
            'status': 00,
            'error': failure_reason
        }

    is_active = True

    if not alias:
        alias = get_random_string(7)
    
    while len(ShortenedURL.objects.filter(unique_id = alias)):
        alias = get_random_string(7)
    
    short_url = f'{data.get("scheme")}://{data.get("domain")}/{alias}'
    try:
        logger.debug("generate_short_url creating new entry in DB")
        new_url = ShortenedURL.objects.create(
            created_dtm=current_timestamp,
            updated_dtm=current_timestamp,
            unique_id=alias,
            original_url = url,
            short_url = short_url,
            domain_name=data.get('domain'),
            expires_at=data.get('expires_at'),
            base_scheme=data.get('base_scheme'),
            base_domain=data.get('base_domain'),
            is_active=is_active
        )
        logger.debug("generate_short_url sending back response")
        return {
            'status': '01',
            'data': {
                'created_at': new_url.created_dtm,
                'original_url': url,
                'short_url': short_url,
                'expires_at': new_url.expires_at,
                'alias': new_url.unique_id,
                'domain': new_url.domain_name,
                'is_active': new_url.is_active,
                'hit_count': new_url.hit_count
            }
        }
    except Exception as e:
        failure_reason = f"generate_short_url error {e}"
        logger.debug(failure_reason)
        return {
            'status': '00',
            'error': failure_reason
        }


def get_original_url_from_unique_id(unique_id):
    url_obj = ShortenedURL.objects.filter(unique_id = unique_id).first()
    if not url_obj:
        return 0, 'Invalid URL'
    if url_obj.expires_at < get_current_dtm():
        return 0, 'URL expired'
    url_obj.hit_count += 1
    url_obj.save()
    
    actual_url = url_obj.original_url
    return 1, actual_url