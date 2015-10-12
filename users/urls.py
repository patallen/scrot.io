from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import ProfileView, WatchWebsiteAjaxView

urlpatterns = [
    url(
        r'^login/$', login,
        {'template_name': 'users/login.html'},
        name='login',
    ),
    url(
        r'^logout/$', logout,
        {'next_page': '/'},
        name='logout',
    ),
    url(
        r'^user/(?P<username>[\w]+)/$', ProfileView.as_view(), name='user_profile'
    ),
    url(r'^ajax/watch/$', WatchWebsiteAjaxView),
]
