from django.db import models


# Store image Urls
class YogaImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
