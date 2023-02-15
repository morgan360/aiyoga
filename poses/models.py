from django.db import models

# Create your models here.
from django.db import models


class PoseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Poses(models.Model):
    english_name = models.CharField(max_length=100)
    sanskrit_name = models.CharField(max_length=100)
    pose_type = models.ManyToManyField(PoseType)

    def __str__(self):
        return f"{self.english_name} ({self.sanskrit_name})"

    class Meta:
        verbose_name_plural = "Poses"
