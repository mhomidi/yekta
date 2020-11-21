from datetime import datetime

from models.visitor.views import AnalyticsView


class OverallTodayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        self.set_find_url_query()
        return self.get_visitors(start_date=datetime.now())


class ByDeviceTodayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        self.set_find_url_query()
        return self.get_visitors(start_date=datetime.now(), device=self.kwargs['device'])


class ByBrowserTodayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        self.set_find_url_query()
        return self.get_visitors(start_date=datetime.now(), browser=self.kwargs['browser'])
