# Servicio de Blog

Este es un microservicio de Blog construido con Django, DRF, PostgreSQL y Redis, todo orquestado con Docker.

## Funcionalidades

* Listado de categorías y posts.
* Detalle de posts.
* Paginación en el listado de posts.
* Búsqueda por texto en título y cuerpo de los posts.
* Caché con Redis para los endpoints de categorías y detalle de post.
* Endpoint de Healthcheck en `/healthz`.
* Logging estructurado en formato JSON por cada petición.

## Cómo ejecutar el proyecto

Este servicio está diseñado para ser ejecutado como parte del `docker-compose.yml` principal del proyecto `microservices-lab`.

### Requisitos

* Docker
* Docker Compose

### Pasos para la ejecución

1.  **Clonar el repositorio (si es necesario):**
    ```bash
    git clone <tu-repositorio>
    ```

2.  **Navegar a la carpeta raíz del proyecto:**
    ```bash
    cd microservices-lab
    ```

3.  **Levantar todos los servicios con Docker Compose:**
    ```bash
    docker-compose up -d --build
    ```
    El servicio de blog estará disponible en `http://localhost:8001`.

### Poblar la Base de Datos (Seed)

Para llenar la base de datos con datos de prueba (autores, categorías y posts), ejecuta el siguiente comando:

```bash
docker-compose run --rm blog python manage.py seed_blog
```

### Endpoints Principales

* `GET /api/categories/`: Lista las categorías.
* `GET /api/posts/`: Lista los posts publicados (paginado).
* `GET /api/posts/?page=2`: Accede a la segunda página de posts.
* `GET /api/posts/?search=palabra`: Busca "palabra" en los posts.
* `GET /api/posts/{slug-del-post}/`: Muestra el detalle de un post.
* `GET /healthz/`: Comprueba el estado del servicio.