from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from .helpers import *


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True,blank=True)
    # image = models.ImageField(upload_to='blog')
    image=models.CharField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)