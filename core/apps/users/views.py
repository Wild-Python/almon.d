from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import RegistrationForm, LoginForm, UpdatePasswordForm
from django.views.decorators.cache import cache_control
from django.contrib import messages


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


# register new user
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account registered successfully. Please log in to your account.")
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


# logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    return redirect('/')
