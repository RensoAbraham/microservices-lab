<<<<<<< HEAD
# Servicio de Autenticación (auth-service)

Este servicio se encarga de la autenticación de usuarios y la generación/validación de tokens JWT. Es un componente fundamental del backend, construido con Django.

## Tecnologías
- Python
- Django
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL (como base de datos)
- Redis (para caching/sesiones)

## Configuración y Ejecución (Desarrollo Local)
Para ejecutar este servicio localmente:
1.  Asegúrate de tener Python y pip instalados.
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Configura las variables de entorno necesarias (puedes ver un ejemplo en el `.env.example` de la raíz del proyecto).
=======
##  Auth Service

Servicio responsable de la **autenticación y autorización** de usuarios dentro del ecosistema.  
Se encarga del registro, inicio de sesión y validación de tokens JWT para el acceso seguro a los demás servicios.

###  Funcionalidades
- Registro de nuevos usuarios  
- Inicio de sesión y validación de credenciales  
- Generación y verificación de tokens JWT  
- Middleware para proteger rutas privadas  

###  Tecnologías
- Node.js + Express  
- MongoDB o PostgreSQL  
- JWT + bcrypt  

###  Estructura
auth-service/
├── src/
│ ├── routes/
│ ├── controllers/
│ ├── models/
│ └── utils/
├── .env
└── package.json

bash
Copiar código

### ▶ Ejecución
```bash
cd auth-service
npm install
npm run start
 Puerto por defecto: 4000

 Endpoints
Método	Ruta	Descripción
POST	/auth/register	Crear un nuevo usuario
POST	/auth/login	Iniciar sesión
GET	/auth/verify	Verificar token JWT
>>>>>>> 04553581254b252a953ff28ca76ac058dc7f2389
