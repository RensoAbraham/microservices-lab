<<<<<<< HEAD
# Laboratorio de Microservicios (Django + React)

Este repositorio contiene un laboratorio de microservicios que demuestra la integración de servicios de backend construidos con Django y una interfaz de usuario frontend desarrollada con React. La arquitectura está diseñada para ser escalable y modular, utilizando un reverse proxy como API Gateway y bases de datos persistentes.

## Arquitectura General

El proyecto se compone de los siguientes servicios principales:

-   **auth-service/**: Servicio de autenticación y gestión de tokens JWT. (Backend)
-   **blog-service/**: Servicio para la gestión de publicaciones, autores y categorías del blog. (Backend)
-   **email-service/**: Servicio para el envío de notificaciones por correo electrónico y gestión de formularios. (Backend)
-   **frontend/**: Interfaz de usuario construida con React. (Frontend)
-   **reverse-proxy/**: Actúa como un balanceador de carga y API Gateway para los servicios de backend. (Infraestructura)

Además, se utilizan los siguientes servicios de base de datos:

-   **PostgreSQL**: Base de datos relacional para la persistencia de datos de los servicios de backend.
-   **Redis**: Base de datos en memoria, utilizada para caching o gestión de sesiones (si aplica).

## Estructura del Proyecto

```
.
├── auth-service/           # Servicio de autenticación (Python/Django)
│   └── README.md
├── blog-service/           # Servicio de blog (Python/Django)
│   └── README.md
├── email-service/          # Servicio de correo electrónico (Python/Django)
│   └── README.md
├── frontend/               # Interfaz de usuario (React)
│   └── README.md
├── reverse-proxy/          # Reverse Proxy / API Gateway (Nginx)
│   └── README.md
├── docker-compose.yml      # Definición de servicios Docker
├── .env.example            # Variables de entorno de ejemplo
├── .gitignore              # Archivos y directorios a ignorar por Git
└── README.md               # Documentación principal del proyecto
```

## Configuración y Ejecución

Para levantar el entorno completo de microservicios, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/RensoDev/microservices-lab.git
    cd microservices-lab
    ```

2.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto, basándote en `.env.example`, y ajusta las variables según sea necesario.

3.  **Construir y levantar los servicios con Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```
    Esto construirá las imágenes de Docker para cada servicio y los iniciará en segundo plano.

## Desarrollo Local

Para desarrollar un servicio individualmente:

1.  Navega al directorio del servicio (ej. `cd auth-service/`).
2.  Instala las dependencias específicas del servicio (ej. `pip install -r requirements.txt` para Python, `npm install` para Node.js/React).
3.  Configura las variables de entorno necesarias para el servicio.
=======
# 🧩 Microservices Lab

**Laboratorio de Microservicios – Stack: Django + React**

---

## 🏗️ Arquitectura general

Cada servicio está aislado y diseñado para comunicarse mediante APIs internas:

- **`auth-service/`** → Manejo de usuarios y autenticación con JWT.  
- **`blog-service/`** → Publicaciones, autores y categorías del sistema.  
- **`email-service/`** → Envío de notificaciones y gestión de formularios.  
- **`frontend/`** → Interfaz desarrollada en React.  
- **`reverse-proxy/`** → Nginx como gateway local y balanceador.

---

## ⚙️ Servicios principales

| Servicio      | Puerto | Descripción                |
|----------------|--------|----------------------------|
| PostgreSQL     | 5432   | Base de datos principal    |
| Redis          | 6379   | Cache y sistema de colas   |

---

## 🧠 Desafío del día

1. Levantar los contenedores:  
   ```bash
   docker compose up -d

2. Crear un archivo de prueba en auth-service/test_connection.py para validar la conexión con PostgreSQL y Redis.

3. Ejecutar la prueba dentro del contenedor correspondiente:
    
   docker exec -it <nombre_del_contenedor> python test_connection.py
>>>>>>> 04553581254b252a953ff28ca76ac058dc7f2389
