from django.conf.urls import url
from .views import (
    HomePageView, RecentScrotsView, WebsiteDetailView, TimelineView
)

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^recent/$', RecentScrotsView.as_view(), name='recent_list'),
    url(
        r'^site/(?P<pk>[0-9]+)/$',
        WebsiteDetailView.as_view(),
        name='website_detail'
    ),
    url(
        r'^site/(?P<pk>[0-9]+)/timeline/$',
        TimelineView.as_view(),
        name='website_timeline'
    ),
]
