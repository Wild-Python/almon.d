from django.urls import path
from core.apps.users import views

app_name = 'users'

urlpatterns = [
    # users account
    # path('', views.UserLoginView.as_view(), name='index'),
    path('', views.user_login_view, name='login'),
    path('register/', views.register_page, name='register-page'),
    path('logout/', views.logout_view, name="logout"),
]