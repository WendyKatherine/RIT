from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from apps.search import views as search_views

# Anotación explícita: django-stubs no infiere bien la mezcla URLPattern|URLResolver
# y se queja con los `+=` de estáticos e i18n_patterns.
urlpatterns: list[URLPattern | URLResolver] = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Rutas localizadas: /es/..., /en/... Wagtail va DENTRO de i18n_patterns para
# que las páginas se sirvan con prefijo de idioma. La raíz "/" redirige al
# idioma por defecto (es).
urlpatterns = urlpatterns + i18n_patterns(
    path("search/", search_views.search, name="search"),
    path("", include(wagtail_urls)),
)
