# Tests del tema — plan de casos

> Estado: pendiente de implementar. 25 asserts en 12 casos.
> Los 11 primeros no tocan base de datos. Solo el 12 la necesita.

## Tabla

| # | Nombre corregido | Qué prueba | Asserts |
|---|---|---|---|
| 1 | `test_no_cookie_resolves_to_light` | Sin cookie, el resolver devuelve `light` | 1 |
| 2 | `test_valid_cookie_is_returned` | Cookie válida se devuelve sin transformar | 1 |
| 3 | `test_invalid_cookie_falls_back_to_light` | Cookie basura cae al default | 1 |
| 4 | `test_next_state_cycles_all_themes` | Orden del ciclo y el retorno a cero | 3 |
| 5 | `test_every_theme_has_a_label` | Cada tema permitido tiene etiqueta en el mapa | 1 |
| 6 | `test_get_returns_405_with_allow_header` | GET rechazado con 405 + `Allow: POST` | 2 |
| 7 | `test_post_valid_theme_sets_cookie_and_redirects` | POST válido: 302, destino y cookie completa | 7 |
| 8 | `test_post_invalid_theme_returns_400_without_cookie` | Tema inválido: 400 y sin cookie | 2 |
| 9 | `test_post_without_csrf_token_returns_403` | Protección CSRF activa | 1 |
| 10 | `test_external_next_falls_back_to_root` | `next` externo descartado | 2 |
| 11 | `test_internal_next_is_preserved` | `next` interno respetado | 2 |
| 12 | `test_page_uses_cookie_theme` | HTML renderizado con `data-theme` de la cookie | 2 |
| — | `test_cookie_is_secure_over_https` (opcional) | Flag `Secure` con request HTTPS | 1 |

## Docstrings

**1. test_no_cookie_resolves_to_light**
Verifica que el resolver use el tema claro cuando la petición no trae cookie.
Cubre la primera visita: `.get()` devuelve `None` y el default no debe filtrarse a la plantilla.

**2. test_valid_cookie_is_returned**
Verifica que una cookie con valor permitido se devuelva sin cambios.
Protege contra un resolver que normalice o sobrescriba una preferencia válida.

**3. test_invalid_cookie_falls_back_to_light**
Verifica que un valor desconocido se reemplace por el default.
Una cookie manipulada no debe llegar al ciclo: `.index` lanzaría `ValueError` y la página sería un 500.

**4. test_next_state_cycles_all_themes**
Verifica el orden del ciclo y el retorno a cero.
`light → dark → system → light`. El último paso es el que fallaba al comparar con `len()` en vez de `len() - 1`.

**5. test_every_theme_has_a_label**
Verifica que cada tema permitido tenga etiqueta en el mapa.
Si falta una clave, el context processor revienta con `KeyError` al indexar el mapa y **todas** las páginas devuelven 500, porque el processor corre en cada request. La etiqueta vacía es el síntoma menor.

**6. test_get_returns_405_with_allow_header**
Verifica que GET se rechace con 405 y cabecera `Allow: POST`.
La respuesta la produce el decorador, no el cuerpo de la vista; la cabecera es lo que hace correcto el rechazo.

**7. test_post_valid_theme_sets_cookie_and_redirects**
Verifica que un POST válido devuelva 302 y persista el tema pedido.
Comprueba los atributos que importan: un año de vida, `Path=/`, `Lax`, `HttpOnly`. El valor debe ser el pedido, no el anterior.

**8. test_post_invalid_theme_returns_400_without_cookie**
Verifica que un tema inválido se rechace antes de escribir la cookie.
Sin `Set-Cookie`: un valor malo no puede persistir un año.

**9. test_post_without_csrf_token_returns_403**
Verifica que el endpoint esté protegido por CSRF.
Requiere un cliente con `enforce_csrf_checks=True`; el cliente por defecto lo omite y ocultaría un token faltante.

**10. test_external_next_falls_back_to_root**
Verifica que un `next` fuera del sitio se descarte.
Guardia de open redirect: `Location` debe quedarse en este host.

**11. test_internal_next_is_preserved**
Verifica que un `next` seguro se respete.
La persona vuelve a la página donde hizo clic, no a la portada.

**12. test_page_uses_cookie_theme**
Verifica que el documento renderizado lleve el atributo del tema.
Caso de integración: necesita base de datos porque renderiza una página de Wagtail. Comprueba 200 y `data-theme` en el HTML.

**Opcional. test_cookie_is_secure_over_https**
Verifica que la cookie lleve `Secure` cuando la petición es HTTPS.
Ata el endpoint a `SECURE_PROXY_SSL_HEADER`: sin él, `is_secure()` es falso detrás del proxy y el flag desaparece en silencio.

## Correcciones al borrador

- `request` como parámetro de test no aporta: es el fixture interno de pytest y acá se sombrea. Usa solo los fixtures que consumes.
- `test_cookie_dark_return_dark` no prueba el resolver: prueba el endpoint. De ahí el nombre nuevo.
- El nombre decía 303 y el código devuelve **302** (`HttpResponseRedirect`). El nombre y el assert deben decir 302, o cambiar la vista a 303.
- Solo el caso 12 necesita `@pytest.mark.django_db`. Marcarlos todos vuelve la suite lenta sin ganar nada.
