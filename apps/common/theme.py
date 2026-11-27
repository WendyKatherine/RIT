from django.http import HttpRequest

theme_values = ("light", "dark", "system")
dic_theme_values = {"light": "claro", "dark": "oscuro", "system": "sistema"}


def get_cookie_theme(request: HttpRequest) -> str:
    cookie_theme = request.COOKIES.get("theme")

    if cookie_theme not in theme_values:
        cookie_theme = "light"
        return cookie_theme
    else:
        return cookie_theme


def theme_next_state(cookie_theme: str) -> str:
    i = theme_values.index(cookie_theme)
    next_value = (i + 1) % len(theme_values)

    return theme_values[next_value]
