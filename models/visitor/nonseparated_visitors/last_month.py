from datetime import datetime, timedelta

import configs
from models.visitor.views import AnalyticsView


class OverallLastMonthAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                            end_date=datetime.now() - timedelta(days=configs.MONTH_PERIOD))



class ByDeviceLastMonthAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                            end_date=datetime.now() - timedelta(days=configs.MONTH_PERIOD),
                                 device=self.kwargs['device'])



class ByBrowserLastMonthAnalyticsView(AnalyticsView):

    def get_queryset(self):
        return self.get_visitors(start_date=datetime.now(),
                            end_date=datetime.now() - timedelta(days=configs.MONTH_PERIOD),
                                 device=self.kwargs['browser'])
