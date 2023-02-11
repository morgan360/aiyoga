from django.db import models


class AiModel(models.Model):
    prompt = models.CharField(max_length=100, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
