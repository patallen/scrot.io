from django.conf.urls import url
from .views import (
    HomePageView, RecentScrotsView, WebsiteDetailView,
    TimelineView, SnapshotDetailView, WebsiteListView,
    CollectionSnapshotsView
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
    url(
        r'^snapshot/(?P<pk>[0-9]+)/$',
        SnapshotDetailView.as_view(),
        name='snapshot_detail'
    ),
    url(
        r'^websites/$',
        WebsiteListView.as_view(),
        name='website_list'
    ),
    url(
        r'^collections/(?P<pk>[0-9]+)/$',
        CollectionSnapshotsView.as_view(),
        name='collection_detail'
    ),
]
