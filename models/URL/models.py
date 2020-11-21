from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q, Count


class URL(models.Model):

    owner = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE)
    address = models.TextField()
    short_addr = models.TextField()

    def get_visitors_in_period(self, start_date=None, end_date=None, device=None, browser=None, separated_user=False):
        query = Q(url=self)
        if start_date:
            first_start_date = datetime(year=start_date.year, month=start_date.month, day=start_date.day)
            query &= Q(date__gt=first_start_date)
        if end_date:
            first_end_date = datetime(year=end_date.year, month=end_date.month, day=end_date.day)
            query &= Q(date__lt=first_end_date)
        if browser:
            query &= Q(browser=browser)
        if device:
            query &= Q(device=device)
        if separated_user:
            return self.visitors.values('url', 'device', 'browser', 'ip').filter(query).annotate(dateCount=Count('date'))
        return self.visitors.filter(query)