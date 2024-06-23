from django.urls import path
from .views import shorten_url, get_original_url


urlpatterns = [
    path('<unique_id>/', get_original_url, name='get_original_url'),
    path('apis/url/create', shorten_url, name='shorten_url')
]
