"""Tests for the light/dark theme layer.

Covers the cookie resolver, the three-state cycle, the label map and the
POST endpoint that persists the choice: method guard, CSRF, cookie
attributes and the open-redirect guard on next.
"""

from django.test import Client, RequestFactory
from django.urls import reverse

from apps.common.theme import dic_theme_values, get_cookie_theme, theme_next_state, theme_values


class TestTheme:
    """Theme resolution, cycle and toggle endpoint."""

    def test_no_cookie_resolves_to_light(self) -> None:
        """Verify that a request without a cookie resolves to light.

        Covers the first-visit path: the cookie lookup returns None and the
        resolver must apply the default instead of returning it.
        """
        request = RequestFactory().get("/")

        assert get_cookie_theme(request) == "light"

    def test_post_invalid_theme_returns_400_without_cookie(self, client: Client) -> None:
        """Verify that an unknown theme is rejected before any cookie is written.

        No Set-Cookie header: a bad value must not persist for a year.
        """
        url = reverse("set_theme", args=["wrongcookie"])
        response = client.post(url, {"next": "/es"})

        assert response.status_code == 400
        assert "theme" not in response.cookies

    def test_invalid_cookie_falls_back_to_light(self) -> None:
        """Verify that a tampered cookie value falls back to the default.

        The value never reaches the cycle, where tuple.index would raise
        ValueError and turn every page into a 500.
        """
        request = RequestFactory().get("/", HTTP_COOKIE="theme=wrongcookie")

        assert get_cookie_theme(request) == "light"

    def test_next_state_cycles_all_themes(self) -> None:
        """Verify the cycle order and its wrap-around.

        light -> dark -> system -> light. The last step is the one that raised
        IndexError when compared against len() instead of len() - 1.
        """
        assert theme_next_state("light") == "dark"
        assert theme_next_state("dark") == "system"
        assert theme_next_state("system") == "light"

    def test_every_theme_has_a_label(self) -> None:
        """Verify that the theme tuple and the label map share the same keys.

        A theme missing from the map makes the context processor raise
        KeyError on every request: a site-wide 500, not just a mute button.
        """
        assert set(theme_values) == set(dic_theme_values)

    def test_get_returns_405_with_allow_header(self, client: Client) -> None:
        """Verify that GET is rejected with 405 and an Allow header.

        The response comes from the decorator, not from the view body; the
        Allow header is what makes the rejection correct per HTTP.
        """
        url = reverse("set_theme", args=["light"])
        response = client.get(url, {"next": "/es"})

        assert response.status_code == 405
        assert response.headers["Allow"] == "POST"

    def test_post_valid_theme_sets_cookie_and_redirects(self, client: Client) -> None:
        """Verify that a valid POST redirects and persists the requested theme.

        Asserts the attributes that matter: one-year max-age, site-wide path,
        SameSite=Lax and HttpOnly. The stored value is the requested theme,
        not the previous one.
        """
        url = reverse("set_theme", args=["dark"])
        response = client.post(url, {"next": "/es/contacto/"})

        assert response.status_code == 302
        assert response["Location"] == "/es/contacto/"

        cookie = response.cookies["theme"]
        assert cookie.value == "dark"
        assert cookie["max-age"] == 31536000
        assert cookie["path"] == "/"
        assert cookie["samesite"] == "Lax"
        assert cookie["httponly"] is True

    def test_post_without_csrf_token_returns_403(self) -> None:
        """Verify that the endpoint requires a CSRF token.

        The default test client disables CSRF checks, so this case needs a
        client created with enforce_csrf_checks=True.
        """
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse("set_theme", args=["dark"]), {"next": "/es/"})

        assert response.status_code == 403

    def test_external_next_falls_back_to_root(self, client: Client) -> None:
        """Verify that an off-site next target is discarded.

        Open-redirect guard: the Location header must stay on this host,
        while the theme is still applied.
        """
        url = reverse("set_theme", args=["dark"])
        response = client.post(url, {"next": "https://evil.com"})

        assert response.status_code == 302
        assert response["Location"] == "/"

    def test_internal_next_is_preserved(self, client: Client) -> None:
        """Verify that a safe next path is honored.

        The user returns to the page where the toggle was clicked instead of
        the home page.
        """
        url = reverse("set_theme", args=["dark"])
        response = client.post(url, {"next": "/es/contacto//"})

        assert response.status_code == 302
        assert response["Location"] == "/es/contacto//"
