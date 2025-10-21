<<<<<<< HEAD
# Frontend (frontend)

Esta es la interfaz de usuario de la aplicación, construida con React. Se comunica con los servicios de backend a través del reverse proxy.

## Tecnologías
- React
- JavaScript/TypeScript
- HTML/CSS
- npm/yarn (gestor de paquetes)

## Configuración y Ejecución (Desarrollo Local)
Para ejecutar este servicio localmente:
1.  Asegúrate de tener Node.js y npm (o yarn) instalados.
2.  Instala las dependencias del proyecto: `npm install` (o `yarn install`)
3.  Configura las variables de entorno necesarias (si aplica, por ejemplo, para la conexión al API Gateway).
=======
## Frontend

Aplicación React que actúa como interfaz principal del sistema.
Consume las APIs de los microservicios mediante el Reverse Proxy.

## Funcionalidades

Registro e inicio de sesión de usuarios

Creación y lectura de publicaciones

Edición y eliminación de contenido propio

Panel de usuario con información de perfil

## Tecnologías

React + Vite

Axios

React Router DOM

TailwindCSS

## Estructura
frontend/
 ├── src/
 │   ├── components/
 │   ├── pages/
 │   ├── services/
 │   └── App.jsx
 ├── .env
 └── package.json

## Ejecución
cd frontend
npm install
npm run dev


 Puerto por defecto: 5173

Configurar la variable VITE_API_URL en .env para apuntar al proxy.
>>>>>>> 04553581254b252a953ff28ca76ac058dc7f2389
