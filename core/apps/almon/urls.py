from django.urls import path
from core.apps.almon import views

app_name = 'almon'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    #  user passwords
    path('add-password/', views.AddNewPasswordView.as_view(), name="add-password"),
    path('manage-passwords/', views.ManagePasswordsView.as_view(), name="manage-passwords"),
    path('update-password/<int:pk>', views.UpdatePasswordView.as_view(), name='update-password'),
    path('delete-password/<int:pk>', views.DeletePasswordView.as_view(), name="delete-password"),
    path('search/', views.SearchPasswordView.as_view(), name='search'),

    # path for generating random password
    path('generate-password/', views.generate_password, name='generate-password'),
]
