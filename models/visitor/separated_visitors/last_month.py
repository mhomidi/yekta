from datetime import datetime, timedelta

import configs
from models.visitor.views import AnalyticsView


class SeparatedOverallLastMonthAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                            end_date=datetime.now() - timedelta(days=configs.MONTH_PERIOD), separated_user=True)


class SeparatedByDeviceLastMonthAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                            end_date=datetime.now() - timedelta(days=configs.MONTH_PERIOD),
                                 device=self.kwargs['device'], separated_user=True)


class SeparatedByBrowserLastMonthAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                            end_date=datetime.now() - timedelta(days=configs.MONTH_PERIOD),
                                 device=self.kwargs['browser'], separated_user=True)
