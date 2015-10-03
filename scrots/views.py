from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from scrots.forms import UrlScrotForm
from .models import Scrot


class HomePageView(FormView):
    form_class = UrlScrotForm
    template_name = 'scrots/index.html'
    success_url = '/'


class RecentScrotsView(ListView):
    template_name = 'scrots/list.html'
    queryset = Scrot.objects.all()


class ScrotDetailView(DetailView):
    template_name = 'scrots/detail.html'
    queryset = Scrot.objects.all()

