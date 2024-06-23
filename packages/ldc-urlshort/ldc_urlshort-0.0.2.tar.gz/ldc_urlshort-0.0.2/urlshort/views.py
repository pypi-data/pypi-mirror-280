from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseRedirect
from .utils import generate_short_url, get_original_url_from_unique_id, get_current_dtm
from .models import ShortenedURL
from .utils import get_base_data
import logging
logger = logging.getLogger("normal")

@api_view(['POST'])
def shorten_url(request):
    try:
        post_data = request.data
        original_url = post_data.get('original_url')
        if not original_url:
            logger.error("shorten_url original_url key is missing in the POST data")
            return JsonResponse({
                'error': 'original_url key is missing in the POST data' 
            })
        
        existing_short_url = ShortenedURL.objects.filter(original_url=original_url,
            expires_at__gt = get_current_dtm()).first()
        if existing_short_url:
            shortened_url = existing_short_url.short_url
            logger.debug(f"shorten_url {shortened_url}")
            return JsonResponse({
                'shortened_url': shortened_url
            })
        
        status, message, data = get_base_data(post_data)
        if not status:
            logger.error(f"shorten_url {message}")
            return JsonResponse({
                'error': message
            })
        logger.debug(f"shorten_url generating short url")
        short_url = generate_short_url(data)
        return JsonResponse(short_url)
    
    except Exception as e:
        logger.debug(f"shorten_url error {e}")
        return JsonResponse({
            'error': 'something went wrong'
        })


@api_view(['GET'])
def get_original_url(_, unique_id):
    try:
        logger.debug(f"get_original_url fetching original url for unique_id {unique_id}")
        status, response = get_original_url_from_unique_id(unique_id)
        if status == 0:
            return JsonResponse({
            'res': response
        })
        logger.debug(f"get_original_url sending back response")
        return HttpResponseRedirect(response)
    except Exception as e:
        logger.debug(f"get_original_url error {e}")
        return JsonResponse({
            'error': 'something went wrong'
        })
    
    