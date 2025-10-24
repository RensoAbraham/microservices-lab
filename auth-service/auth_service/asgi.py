import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_service.settings')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRoute

aplication = ProtocolTypeRoute({    
    'http': django_asgi_app,
})