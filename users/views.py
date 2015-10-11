from django.views.generic import DetailView
from django.http import Http404

from .models import CustomUser


class ProfileView(DetailView):
    template_name = 'users/profile.html'
    model = CustomUser

    def get_object(self):
        username = self.kwargs.get('username', None)
        queryset = self.get_queryset()

        queryset = queryset.filter(username=username)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': queryset.model._meta.verbose_name})

        return obj
