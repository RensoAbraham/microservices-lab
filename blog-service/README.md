<<<<<<< HEAD
# Servicio de Blog (blog-service)

Este servicio gestiona las publicaciones del blog, incluyendo autores, categorías y el contenido de los artículos. Es un componente fundamental del backend, construido con Django.

## Tecnologías
- Python
- Django
- Django REST Framework
- PostgreSQL (como base de datos)

## Configuración y Ejecución (Desarrollo Local)
Para ejecutar este servicio localmente:
1.  Asegúrate de tener Python y pip instalados.
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Configura las variables de entorno necesarias (puedes ver un ejemplo en el `.env.example` de la raíz del proyecto).
=======
## Blog Service

Servicio encargado de la gestión de publicaciones, autores y comentarios.
Depende del Auth Service para validar la identidad de los usuarios.

## Funcionalidades

CRUD de publicaciones

Comentarios y etiquetas

Búsqueda y filtrado

Validación JWT con Auth Service

## Tecnologías

Node.js + Express

MongoDB

Axios + JWT

## Estructura
blog-service/
 ├── src/
 │   ├── routes/
 │   ├── controllers/
 │   ├── models/
 │   └── middleware/
 ├── .env
 └── package.json

## Ejecución
cd blog-service
npm install
npm run start


 Puerto por defecto: 4001

## Endpoints
Método	Ruta	Descripción
GET	/posts	Listar publicaciones
POST	/posts	Crear nueva publicación
PUT	/posts/:id	Actualizar publicación
DELETE	/posts/:id	Eliminar publicación
>>>>>>> 04553581254b252a953ff28ca76ac058dc7f2389
