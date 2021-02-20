from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=255)
    Text_description = models.CharField(max_length=255)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('hello:detail',kwargs={'pk':self.pk})