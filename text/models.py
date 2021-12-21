from django.db import models
from taggit.managers import TaggableManager

class Image(models.Model):
    tags = TaggableManager()
    image = models.ImageField(upload_to='images')