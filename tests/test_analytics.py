"""Analitica: se enciende solo en produccion (SEO_INDEXABLE) y con IDs."""

import pytest


@pytest.mark.django_db
def test_sin_analitica_en_entorno_no_indexable(client):
    response = client.get("/es/")
    assert response.status_code == 200
    html = response.content.decode()
    assert "googletagmanager.com" not in html
    assert "analytics-events.js" not in html


@pytest.mark.django_db
def test_gtm_cuando_hay_contenedor(client, settings):
    settings.SEO_INDEXABLE = True
    settings.GTM_ID = "GTM-TEST123"
    settings.GA4_MEASUREMENT_ID = ""
    html = client.get("/es/").content.decode()
    assert "googletagmanager.com/gtm.js?" in html
    assert 'dataLayer", "GTM-TEST123"' in html
    assert "analytics-events.js" in html


@pytest.mark.django_db
def test_ga4_directo_sin_gtm(client, settings):
    settings.SEO_INDEXABLE = True
    settings.GTM_ID = ""
    settings.GA4_MEASUREMENT_ID = "G-TEST123"
    html = client.get("/es/").content.decode()
    assert "gtag/js?id=G-TEST123" in html
    assert "gtm.js" not in html
