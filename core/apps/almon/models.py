from django.db import models
from django.conf import settings
from .cryptor import Cryptor
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Almon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

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

    def __str__(self):
        return f'{self.user}'
