import contextlib

from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

from .base import *

SECRET_KEY = env("DJANGO_SECRET_KEY")  # requerida (sin default: falla si falta)
DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")  # requerida

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage


class NonStrictManifestStaticFilesStorage(ManifestStaticFilesStorage):
    """Manifest que no tumba la web si falta una entrada.

    Si `collectstatic` se ejecuta con los settings equivocados (p. ej. los de
    dev), `staticfiles.json` queda desactualizado y cada `{% static %}` de un
    asset nuevo lanzaba `ValueError` -> 500 en todo el sitio. Con
    `manifest_strict = False` se sirve la ruta sin hash (el archivo existe
    igual) y la página sigue funcionando.
    """

    manifest_strict = False


STORAGES["staticfiles"]["BACKEND"] = (
    "config.settings.production.NonStrictManifestStaticFilesStorage"
)


with contextlib.suppress(ImportError):
    from .local import *
