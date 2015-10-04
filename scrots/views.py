from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from scrots.forms import UrlScrotForm
from .models import Scrot
from wappa.pages import get_screenshot_from_url


class HomePageView(FormView):
    form_class = UrlScrotForm
    template_name = 'scrots/index.html'

    def form_valid(self, form):
        print("Form was valid")
        url = form.data['url']
        self.scrot = get_screenshot_from_url(url)
        return super(HomePageView, self).form_valid(form)

    def get_success_url(self):
        url = '/scrot/{}'.format(self.scrot.id)
        return url


class RecentScrotsView(ListView):
    template_name = 'scrots/list.html'
    queryset = Scrot.objects.all()


class ScrotDetailView(DetailView):
    template_name = 'scrots/detail.html'
    queryset = Scrot.objects.all()
