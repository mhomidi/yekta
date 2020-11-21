from datetime import datetime, timedelta

import configs
from models.visitor.views import AnalyticsView


class OverallLastWeekAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.WEEK_PERIOD))


class ByDeviceLastWeekAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.WEEK_PERIOD),
                                 device=self.kwargs['device'])


class ByBrowserLastWeekAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.WEEK_PERIOD),
                                 device=self.kwargs['browser'])
