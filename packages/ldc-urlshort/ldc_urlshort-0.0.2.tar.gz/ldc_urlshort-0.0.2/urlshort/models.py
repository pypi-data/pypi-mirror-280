from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=300, db_index=True)
    short_url = models.CharField(max_length=60, unique=True)
    created_dtm = models.DateTimeField(auto_now_add=True)
    updated_dtm = models.DateTimeField(auto_now=True)
    unique_id = models.CharField(max_length=30, db_index=True, unique=True)
    hit_count = models.IntegerField(default=0)
    expires_at = models.DateTimeField(null=True)
    domain_name = models.CharField(max_length=100, null=True)
    base_scheme = models.CharField(max_length=30, null=True)
    base_domain = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)