from django.db import models
from django.db.models import *
from django.conf import settings
from django.utils import timezone
# Create your models here.
from CollegeSpace import settings
from django.utils.text import slugify


class Question(models.Model):
    question = TextField()
    question_data = TextField(blank=True, null=True, default=" ")
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_date = DateTimeField(default=timezone.now)
    slug = SlugField(blank=True, null=True)
    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.question)
        
        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    answer = TextField()
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answered_date = DateTimeField(default=timezone.now)
    question = ForeignKey(Question, on_delete=models.CASCADE)
    status = BooleanField(default=False)

    def __str__(self):
        return self.answer