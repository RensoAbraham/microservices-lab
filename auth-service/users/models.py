# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Por ahora no añadiremos campos extra, pero la estructura ya está lista.
    # Simplemente pasamos.
    pass