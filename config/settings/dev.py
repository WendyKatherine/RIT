import contextlib

from .base import *

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-solo-desarrollo")
DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])


with contextlib.suppress(ImportError):
    from .local import *
