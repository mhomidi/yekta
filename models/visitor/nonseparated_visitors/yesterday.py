from datetime import datetime, timedelta

import configs
from models.visitor.views import AnalyticsView


class OverallYesterdayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.DAY_PERIOD))


class ByDeviceYesterdayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.DAY_PERIOD),
                                 device=self.kwargs['device'])


class ByBrowserYesterdayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.DAY_PERIOD),
                                 device=self.kwargs['browser'])