"""Contrato de settings: el entorno del hijo define DEBUG y ALLOWED_HOSTS."""

import json
import os
import subprocess
import sys


class TestSettingsContract:
    def test_dev_settings_read_debug_and_hosts_from_env(self) -> None:
        """El hijo lee DJANGO_DEBUG y DJANGO_ALLOWED_HOSTS del entorno, no del shell."""
        root_project = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # 1. Entorno limpio y explícito: nada de DJANGO_* heredado del shell.
        env_sub_process = os.environ.copy()
        for key in list(env_sub_process):
            if key.startswith("DJANGO_"):
                del env_sub_process[key]

        env_sub_process.update(
            {
                "DJANGO_SETTINGS_MODULE": "config.settings.dev",
                "DJANGO_DEBUG": "False",
                "DJANGO_ALLOWED_HOSTS": "localhost,127.0.0.1",
                # base.py hace env.db("DATABASE_URL") al importar: sin esto el hijo
                # ni siquiera llega a leer DEBUG. No se conecta a la base.
                "DATABASE_URL": "postgres://rit:rit@localhost:5433/rit_website",
                "PYTHONPATH": root_project,
            }
        )

        # 2. El código va como SEGUNDO argumento de -c (antes faltaba).
        child_code = (
            "import json\n"
            "import django\n"
            "django.setup()\n"
            "from django.conf import settings\n"
            "print(json.dumps({\n"
            "    'debug': settings.DEBUG,\n"
            "    'allowed_hosts': settings.ALLOWED_HOSTS,\n"
            "}))\n"
        )

        result = subprocess.run(
            [sys.executable, "-c", child_code],
            cwd=root_project,
            env=env_sub_process,
            capture_output=True,
            text=True,
        )

        # 3. Comparaciones reales, no tuplas (una tupla no vacía siempre es True).
        assert result.returncode == 0, f"Error en el hijo: {result.stderr}"

        data_received = json.loads(result.stdout.strip())

        assert data_received["debug"] is False
        assert data_received["allowed_hosts"] == ["localhost", "127.0.0.1"]
