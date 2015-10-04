from django.conf.urls import url
from .views import HomePageView, RecentScrotsView, ScrotDetailView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^recent/$', RecentScrotsView.as_view(), name='recent_list'),
    url(
        r'^scrot/(?P<pk>[0-9]+)/$',
        ScrotDetailView.as_view(),
        name='scrot_detail'
    ),
]
