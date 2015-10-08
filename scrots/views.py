from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView

from screenshotter.handlers import ScrotHandler
from .forms import UrlScrotForm
from .models import Scrot, Website


class HomePageView(FormView):
    form_class = UrlScrotForm
    template_name = 'scrots/index.html'

    def form_valid(self, form):
        url = form.data['url']
        scrot = ScrotHandler(url)
        domain = scrot.domain
        self.website, _ = Website.objects.get_or_create(domain=domain)
        self.website.add_snapshot()
        return super(HomePageView, self).form_valid(form)

    def get_success_url(self):
        url = reverse('website_detail', kwargs={'pk': self.website.id})
        return url


class RecentScrotsView(ListView):
    template_name = 'scrots/list.html'
    queryset = Website.objects.order_by('-create_date')


class WebsiteDetailView(DetailView):
    template_name = 'scrots/detail.html'
    queryset = Website.objects.all()
