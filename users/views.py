from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect

from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.http import Http404,  HttpResponseForbidden, HttpResponse

from .models import CustomUser
from .forms import RegistrationForm
from scrots.models import Website


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


class RegisterView(CreateView):
    form_class = RegistrationForm
    success_url = "/login/"
    template_name = "users/register.html"

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.set_password(self.object.password)
            self.object.save()
            messages.add_message(
                self.request,
                messages.SUCCESS,
                "Success! You man now log in."
            )
        except:
            messages.add_message(
                self.request,
                messages.ERROR,
                "There was a problem creating your account."
            )
            return redirect("user_registration")
        return super(RegisterView, self).form_valid(form)


@login_required
def WatchWebsiteAjaxView(request):
    if request.method == "POST":
        website_id = request.POST.get('website_id', None)
        user = request.user
        website = get_object_or_404(Website, id=website_id)
        if user.likes_website(website):
            user.watched_websites.remove(website)
            res_text = "Website has been removed from watchlist."
        else:
            user.watched_websites.add(website)
            res_text = "Website has been added to watchlist."
        return HttpResponse(res_text)
    else:
        return HttpResponseForbidden("Method Not Allowed")
