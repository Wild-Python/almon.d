from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, get_user_model
from .forms import RegistrationForm, LoginForm, UpdatePasswordForm
from django.views.decorators.cache import cache_control
from django.contrib import messages

from .tokens import Token_Generator
from .mixins import OnlyUnauthenticatedMixin
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse

User = get_user_model()


class UserAccountEmailConfirmView(TemplateView):
    template_name = 'users/registration/register_email_confirm.html'


class UserAccountActivationView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            user_id = urlsafe_base64_decode(kwargs['uid']).decode()
            user = User.objects.get(pk=user_id)

            if Token_Generator.check_token(user, kwargs['token']):
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('User is already active!')

            else:
                return HttpResponse('Activation link is invalid!')

        except User.DoesNotExist:
            return HttpResponse('User not found!')

        except (KeyError, TypeError, ValueError):
            return HttpResponse('Error in activation!')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        print(form.cleaned_data['username'])
        return super(UserLoginView, self).form_valid(form)


def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return UserLoginView.as_view()(request)


def reverse_lazy(param):
    pass


class UserRegistrationView(CreateView, OnlyUnauthenticatedMixin):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = '/users/confirm-email/'

    def get_form_kwargs(self):
        """Send request to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    return redirect('/')
