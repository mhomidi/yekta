from datetime import datetime, timedelta

# Create your views here.
from rest_framework import generics

import configs
from models.URL.models import URL
from models.visitor.serializers import VisitorSerializer


class AnalyticsView(generics.ListAPIView):

    serializer_class = VisitorSerializer
    find_url_query = None

    def set_find_url_query(self):
        self.find_url_query = URL.objects.filter(id=int(self.kwargs['url_id']), owner=self.request.user)

    def get_visitors(self, start_date=None, end_date=None, device=None, browser=None, separated_user=False):
        self.set_find_url_query()
        if self.find_url_query:
            url = self.find_url_query.first()
            return url.get_visitors_in_period(start_date=start_date, end_date=end_date,
                                              device=device, browser=browser, separated_user=separated_user)
        return self.find_url_query
