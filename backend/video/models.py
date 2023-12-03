from django.db import models

# Create your models here.
class VideoFolder(models.Model):
    relative_path = models.CharField(max_length=512)
    video_count = models.IntegerField()
    info = models.JSONField()
