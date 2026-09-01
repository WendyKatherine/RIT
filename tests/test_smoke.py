import pytest
from django.test import Client


@pytest.mark.django_db
def test_root_redirects_to_default_language(client: Client) -> None:
    """La raíz redirige al idioma por defecto (es) gracias a i18n_patterns."""
    response = client.get("/")
    assert response.status_code in (200, 301, 302)
    assert "/es/" in response.headers.get("location", "/es/")


@pytest.mark.django_db
def test_home_es_returns_200(client: Client) -> None:
    """La Home en español responde correctamente."""
    assert client.get("/es/").status_code == 200


@pytest.mark.django_db
def test_admin_login_returns_200(client: Client) -> None:
    """El login del admin de Wagtail está accesible."""
    assert client.get("/admin/login/").status_code == 200
