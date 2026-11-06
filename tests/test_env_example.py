"""Configuration contract between .env.example and Django settings."""

from pathlib import Path

file_path = Path(__file__).resolve().parents[1] / ".env.example"


class TestEnvExample:
    def test_env_example_declares_prefixed_names(self) -> None:
        """Falla si falta una clave DJANGO_ o si aparece una clave sin prefijo."""
        result_allowed = []
        result_not_allowed = []
        allowed = ("DJANGO_SECRET_KEY=", "DJANGO_DEBUG=", "DJANGO_ALLOWED_HOSTS=")
        not_allowed = ("SECRET_KEY=", "DEBUG=", "ALLOWED_HOSTS=")

        with open(file_path, encoding="utf-8") as file:
            content = file.readlines()

        for line in content:
            for w in allowed:
                search_lines_allowed = line.startswith(w)
                if search_lines_allowed:
                    result_allowed.append(w)

            search_lines_not_allowed = line.startswith(not_allowed)
            result_not_allowed.append(search_lines_not_allowed)

        comparison_allowed = set(allowed) == set(result_allowed)

        assert comparison_allowed
        assert not any(result_not_allowed)
