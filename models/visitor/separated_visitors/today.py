from datetime import datetime

from models.visitor.views import AnalyticsView


class SeparatedOverallTodayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        self.set_find_url_query()
        return self.get_visitors(start_date=datetime.now(), separated_user=True)


class SeparatedByDeviceTodayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        self.set_find_url_query()
        return self.get_visitors(start_date=datetime.now(), device=self.kwargs['device'], separated_user=True)


class SeparatedByBrowserTodayAnalyticsView(AnalyticsView):

    def get_queryset(self):
        self.set_find_url_query()
        return self.get_visitors(start_date=datetime.now(), browser=self.kwargs['browser'], separated_user=True)
