from datetime import datetime

from django.db import models

# Create your models here.
from models.URL.models import URL


class Visitor(models.Model):

    MOBILE = 1
    DESKTOP = 2

    DEVICES = (
        (MOBILE, 'Mobile'),
        (DESKTOP, 'Desktop'),
    )
    url = models.ForeignKey(URL, related_name='visitors', on_delete=models.CASCADE)
    device = models.IntegerField(choices=DEVICES, default=DESKTOP)
    browser = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now())
    ip = models.CharField(max_length=17, default='127.0.0.1')

