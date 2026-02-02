from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from .forms import CreateUserForm

# Create your views here.

# Landing Page
class IndexView(TemplateView):
    template_name = 'texcably_app/index.html'


# App Main Page
class AppIndexView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        return render(request, 'texcably_app/app_index.html')


# User Authentication
class CreateAccountView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'texcably_app/create_account.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'texcably_app/login.html'

    def get_success_url(self):
        return reverse_lazy('app_index')


class UserLogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('login'))