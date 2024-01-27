

from django.contrib.auth.base_user import BaseUserManager


def generate_random_password():
    return BaseUserManager().make_random_password()
