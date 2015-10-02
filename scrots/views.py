from django.views.generic.edit import FormView
from scrots.forms import UrlScrotForm


class HomePageView(FormView):
    form_class = UrlScrotForm
    template_name = 'scrots/index.html'
    success_url = '/'
