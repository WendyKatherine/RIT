"""Pruebas de las senales SEO por entorno."""

import pytest
from django.test import Client, override_settings


@pytest.mark.django_db
def test_robots_bloquea_por_defecto(client: Client) -> None:
    """Sin SEO_INDEXABLE (local/staging) todo queda bloqueado."""
    response = client.get("/robots.txt")
    body = response.content.decode()
    assert response.status_code == 200
    assert "Disallow: /" in body
    assert "Sitemap:" not in body


@pytest.mark.django_db
@override_settings(SEO_INDEXABLE=True, SITE_URL="https://ritenterprise.com.co")
def test_robots_permisivo_en_produccion(client: Client) -> None:
    response = client.get("/robots.txt")
    body = response.content.decode()
    assert response.status_code == 200
    assert "User-agent: *" in body
    assert "Allow: /" in body
    assert "GPTBot" in body
    assert "Sitemap: https://ritenterprise.com.co/sitemap.xml" in body


@pytest.mark.django_db
def test_sitemap_responde(client: Client) -> None:
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert b"<urlset" in response.content


@pytest.mark.django_db
@override_settings(SEO_INDEXABLE=True, SITE_URL="https://ritenterprise.com.co")
def test_home_expone_canonical_og_y_jsonld(client: Client) -> None:
    response = client.get("/es/")
    assert response.status_code == 200
    html = response.content.decode()
    assert '<link rel="canonical" href="https://ritenterprise.com.co/es/">' in html
    assert 'property="og:url"' in html
    assert 'name="twitter:card"' in html
    assert "application/ld+json" in html
    assert '"@type": "Organization"' in html
    assert "901.106.159-8" in html
    assert 'content="index, follow' in html


@pytest.mark.django_db
def test_home_marca_noindex_fuera_de_produccion(client: Client) -> None:
    response = client.get("/es/")
    assert response.headers.get("X-Robots-Tag") == "noindex, nofollow"
    assert "noindex, nofollow" in response.content.decode()
