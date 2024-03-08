from django.db import models
from django.conf import settings
from .cryptor import Cryptor


class Almon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False, blank=False)

    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)

    application_type = models.CharField(max_length=30)
    application_name = models.CharField(max_length=30, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)

    @property
    def decrypted_email(self):
        return Cryptor.decrypt(self.email)

    @property
    def decrypted_password(self):
        return Cryptor.decrypt(self.password)
