from django.urls import path

from models.visitor.nonseparated_visitors.last_month import *
from models.visitor.nonseparated_visitors.last_week import *
from models.visitor.nonseparated_visitors.today import *
from models.visitor.nonseparated_visitors.yesterday import *
from models.visitor.separated_visitors.last_month import *
from models.visitor.separated_visitors.last_week import *
from models.visitor.separated_visitors.today import *
from models.visitor.separated_visitors.yesterday import *

urlpatterns = [

    path('<int:url_id>/today', OverallTodayAnalyticsView.as_view()),
    path('<int:url_id>/yesterday', OverallYesterdayAnalyticsView.as_view()),
    path('<int:url_id>/week', OverallLastWeekAnalyticsView.as_view()),
    path('<int:url_id>/month', OverallLastMonthAnalyticsView.as_view()),

    path('<int:url_id>/today/<int:device>', ByDeviceTodayAnalyticsView.as_view()),
    path('<int:url_id>/yesterday/<int:device>', ByDeviceYesterdayAnalyticsView.as_view()),
    path('<int:url_id>/week/<int:device>', ByDeviceLastWeekAnalyticsView.as_view()),
    path('<int:url_id>/month/<int:device>', ByDeviceLastMonthAnalyticsView.as_view()),

    path('<int:url_id>/today/<slug:browser>', ByBrowserTodayAnalyticsView.as_view()),
    path('<int:url_id>/yesterday/<slug:browser>', ByBrowserYesterdayAnalyticsView.as_view()),
    path('<int:url_id>/week/<slug:browser>', ByBrowserLastWeekAnalyticsView.as_view()),
    path('<int:url_id>/month/<slug:browser>', ByBrowserLastMonthAnalyticsView.as_view()),

    path('separate/<int:url_id>/today', SeparatedOverallTodayAnalyticsView.as_view()),
    path('separate/<int:url_id>/yesterday', SeparatedOverallYesterdayAnalyticsView.as_view()),
    path('separate/<int:url_id>/week', SeparatedOverallLastWeekAnalyticsView.as_view()),
    path('separate/<int:url_id>/month', SeparatedOverallLastMonthAnalyticsView.as_view()),

    path('separate/<int:url_id>/today/<int:device>', SeparatedByDeviceTodayAnalyticsView.as_view()),
    path('separate/<int:url_id>/yesterday/<int:device>', SeparatedByDeviceYesterdayAnalyticsView.as_view()),
    path('separate/<int:url_id>/week/<int:device>', SeparatedByDeviceLastWeekAnalyticsView.as_view()),
    path('separate/<int:url_id>/month/<int:device>', SeparatedByDeviceLastMonthAnalyticsView.as_view()),

    path('separate/<int:url_id>/today/<slug:browser>', SeparatedByBrowserTodayAnalyticsView.as_view()),
    path('separate/<int:url_id>/yesterday/<slug:browser>', SeparatedByBrowserYesterdayAnalyticsView.as_view()),
    path('separate/<int:url_id>/week/<slug:browser>', SeparatedByBrowserLastWeekAnalyticsView.as_view()),
    path('separate/<int:url_id>/month/<slug:browser>', SeparatedByBrowserLastMonthAnalyticsView.as_view()),
]
