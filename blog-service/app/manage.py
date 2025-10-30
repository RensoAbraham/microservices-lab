#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_service.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
             "No se ha podido importar Django. ¿Estas seguro de que esta instalado"
             "y disponible en tu variable de entorno PYTHONPATH? ¿Has olvidado activar"
             "un entorno virtual?"    
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
