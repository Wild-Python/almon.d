from django.urls import path
from core.apps.users import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .forms import PasswdResetConfirmForm, PasswdResetForm

app_name = 'users'

urlpatterns = [
    # users account
    # path('', views.UserLoginView.as_view(), name='index'),
    path('login/', views.user_login_view, name='login'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('logout/', views.logout_view, name="logout"),

    # account activation urls
    path('confirm-email/', views.UserAccountEmailConfirmView.as_view(), name='confirm-email'),
    path('activate/<uid>/<token>/', views.UserAccountActivationView.as_view(), name='activate'),

    # Password reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password-reset/password_reset_form.html',
        email_template_name='users/password-reset/password_reset_email.html',
        success_url='password-reset-email-confirm/',
        form_class=PasswdResetForm
    ), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password-reset/password_reset_confirm.html',
        success_url='/password-reset-complete/',
        form_class=PasswdResetConfirmForm
    ), name='password_reset_confirm'),
    path('password-reset/password-reset-email-confirm/',
         TemplateView.as_view(template_name="users/password-reset/reset_status.html"),
         name='password_reset_done'),
    path('password-reset/password-reset-complete/',
         TemplateView.as_view(template_name="users/password-reset/reset_status.html"),
         name='password_reset_complete'),
]
