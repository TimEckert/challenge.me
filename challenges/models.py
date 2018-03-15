from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class Challenge(models.Model):
#all class object attributes?
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    teaser = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    archived_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
