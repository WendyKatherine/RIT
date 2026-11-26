"""Analitica: se enciende solo en produccion (SEO_INDEXABLE) y con IDs."""

import pytest
from django.test import Client, override_settings


@pytest.mark.django_db
def test_sin_analitica_en_entorno_no_indexable(client: Client) -> None:
    """Local/staging: no se carga nada de Google."""
    html = client.get("/es/").content.decode()
    assert "googletagmanager.com" not in html
    assert "analytics-events.js" not in html


@pytest.mark.django_db
@override_settings(SEO_INDEXABLE=True, GTM_ID="GTM-TEST123", GA4_MEASUREMENT_ID="")
def test_gtm_cuando_hay_contenedor(client: Client) -> None:
    """Con GTM_ID se carga el contenedor y el JS de eventos."""
    html = client.get("/es/").content.decode()
    assert "googletagmanager.com/gtm.js?" in html
    assert 'dataLayer", "GTM-TEST123"' in html
    assert "analytics-events.js" in html


@pytest.mark.django_db
@override_settings(SEO_INDEXABLE=True, GTM_ID="", GA4_MEASUREMENT_ID="G-TEST123")
def test_ga4_directo_sin_gtm(client: Client) -> None:
    """Sin GTM cae a gtag.js directo con el ID de GA4."""
    html = client.get("/es/").content.decode()
    assert "gtag/js?id=G-TEST123" in html
    assert "gtm.js?" not in html
