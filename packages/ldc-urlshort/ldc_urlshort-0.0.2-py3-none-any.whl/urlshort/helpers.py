from .utils import generate_short_url, get_original_url_from_unique_id
from .models import ShortenedURL
from .utils import get_base_data, get_current_dtm
import logging
logger = logging.getLogger("normal")

def shorten_url(original_url):
    try:
        if not original_url:
            failure_reason = "shorten_url original_url is missing in the POST data"
            logger.error(failure_reason)
            return {
                'error': failure_reason
            }
        existing_short_url = ShortenedURL.objects.filter(original_url=original_url,
            expires_at__gt = get_current_dtm()).first()
        if existing_short_url:
            shortened_url = existing_short_url.short_url
            logger.debug(f"shorten_url {shortened_url}")
            return {
                "data": {
                    "short_url": shortened_url
                }
            }
        data_dict = {
            "original_url": original_url
        }
        status, message, data = get_base_data(data_dict)
        if not status:
            logger.error(f"shorten_url {message}")
            return {
                'error': message
            }
        logger.debug(f"shorten_url generating short url")
        short_url = generate_short_url(data)
        return short_url
    except Exception as e:
        logger.debug(f"shorten_url error {e}")
        return {
            'error': 'something went wrong'
        }


def get_original_url(unique_id):
    try:
        status, response = get_original_url_from_unique_id(unique_id)
        return {
            'status': status,
            'res': response
        }
    except Exception as e:
        logger.debug(f"get_original_error error {e}")
        return {
            'error': 'something went wrong'
        }

