from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.apps.almon.urls', namespace='almon')),
    path('users/', include('core.apps.users.urls', namespace='users')),
]
