from django import template
from core.apps.almon.cryptor import Cryptor

register = template.Library()


@register.filter
def decrypt_password(password):
    return Cryptor.decrypt(password)
