from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView

from screenshotter.handlers import ScrotHandler
from .forms import UrlScrotForm
from .models import Scrot


class HomePageView(FormView):
    form_class = UrlScrotForm
    template_name = 'scrots/index.html'

    def form_valid(self, form):
        url = form.data['url']
        scrot = ScrotHandler(url)
        scrot.create_images()
        self.scrot = scrot.save_to_db()
        return super(HomePageView, self).form_valid(form)

    def get_success_url(self):
        url = reverse('scrot_detail', kwargs={'pk': self.scrot.id})
        return url


class RecentScrotsView(ListView):
    template_name = 'scrots/list.html'
    queryset = Scrot.objects.all()


class ScrotDetailView(DetailView):
    template_name = 'scrots/detail.html'
    queryset = Scrot.objects.all()
