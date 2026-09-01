from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Usuario personalizado del sitio.

    Hereda todo de Django (auth, grupos, permisos) — listo para crecer
    (rol, teléfono, empresa…).
    """

    pass
