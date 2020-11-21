from datetime import datetime, timedelta

import configs
from models.visitor.views import AnalyticsView


class SeparatedOverallLastWeekAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.WEEK_PERIOD), separated_user=True)


class SeparatedByDeviceLastWeekAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.WEEK_PERIOD),
                                 device=self.kwargs['device'], separated_user=True)


class SeparatedByBrowserLastWeekAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                                 end_date=datetime.now() - timedelta(days=configs.WEEK_PERIOD),
                                 device=self.kwargs['browser'], separated_user=True)
