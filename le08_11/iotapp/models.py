import os

from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.db import models

# Create your models here.
from twilio.rest import Client


class don(models.Model):
    ta = models.FloatField(null=True)
    ha = models.FloatField(null=True)
    tmp = models.FloatField(null=True)
    lux = models.FloatField(null=True)
    tg = models.FloatField(null=True)

    qua = models.FloatField(null=True)
    onf = models.IntegerField(null=True)
    sm = models.IntegerField(null=True)
    p = models.IntegerField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.ta)

