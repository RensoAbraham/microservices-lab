# Servicio de Correo Electrónico (email-service)

Este servicio es responsable del envío de notificaciones por correo electrónico y la gestión de formularios de contacto. Es un componente fundamental del backend, construido con Django.

## Tecnologías
- Python
- Django
- Django REST Framework (para API si aplica)
- Librería de envío de correos (ej. `django.core.mail`)
- PostgreSQL (como base de datos)
- Redis (para caching/colas de mensajes si aplica)

## Configuración y Ejecución (Desarrollo Local)
Para ejecutar este servicio localmente:
1.  Asegúrate de tener Python y pip instalados.
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Configura las variables de entorno necesarias (puedes ver un ejemplo en el `.env.example` de la raíz del proyecto).