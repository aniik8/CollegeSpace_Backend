from typing import Text
from django.conf import settings
from django.db import models
from django.db.models import *
from django.utils import timezone
from CollegeSpace import settings
from django.conf import settings
from django.utils.text import slugify

class Notes(models.Model):
    notes_title = TextField(max_length=30)
    notes_content = TextField()
    created = DateTimeField(default=timezone.now)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = SlugField(blank=True, null=True)


    def __str__(self):
        return self.notes_title
    
    
    def save(self, *args, **kwargs):

        if self.slug is None:
            self.slug = slugify(self.notes_title)
            
        super(Notes,self).save(*args, **kwargs)