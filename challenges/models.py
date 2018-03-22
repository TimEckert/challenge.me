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
    challenge_start = models.DateTimeField(
            blank=True, null=True)
    challenge_stop = models.DateTimeField(
            blank=True, null=True)
    challenge_active = models.BooleanField(
            default=False) 


    def publish(self):
        self.challenge_start = timezone.now()
        self.save()

    def __str__(self):
        return self.title
