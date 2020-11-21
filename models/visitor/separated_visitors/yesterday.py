from datetime import datetime, timedelta

import configs
from models.visitor.views import AnalyticsView


class SeparatedOverallYesterdayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.DAY_PERIOD),
                                 separated_user=True)


class SeparatedByDeviceYesterdayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.DAY_PERIOD),
                                 device=self.kwargs['device'], separated_user=True)


class SeparatedByBrowserYesterdayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.DAY_PERIOD),
                                 device=self.kwargs['browser'], separated_user=True)