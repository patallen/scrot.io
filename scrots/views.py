from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView

from screenshotter.handlers import ScrotHandler
from .forms import UrlScrotForm
from .models import Website, Snapshot


class FormListView(FormView, ListView):
    """
    View Mixin that adds a form to a ListView
    """
    def get_context_data(self, **data):
        context = super(FormListView, self).get_context_data(**data)
        context['form'] = self.get_form(self.form_class)
        return context


class HomePageView(FormListView):
    form_class = UrlScrotForm
    template_name = 'scrots/index.html'
    queryset = Snapshot.objects.order_by('-date_taken')[:6]

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


class TimelineView(ListView):
    """
    Returns a list of snapshots based on the website PK provided in the URL.
    We override get_context_data to add the website as 'object' in context.
    """
    template_name = 'scrots/timeline.html'

    def get_queryset(self, *args, **kwargs):
        self.object = Website.objects.filter(id=self.kwargs['pk']).first()
        return self.object.snapshot_set.order_by('-date_taken')

    def get_context_data(self, **kwargs):
        context = super(TimelineView, self).get_context_data(**kwargs)
        context['object'] = self.object
        return context


class SnapshotDetailView(DetailView):
    model = Snapshot
    template_name = 'scrots/snapshot.html'
