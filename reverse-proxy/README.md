<<<<<<< HEAD
# Reverse Proxy / API Gateway (reverse-proxy)

Este componente actúa como un proxy inverso y una puerta de enlace API para los servicios de backend. Gestiona el enrutamiento de solicitudes y el balanceo de carga.

## Tecnologías
- Docker (para orquestación)

## Configuración y Ejecución (Desarrollo Local)
Para ejecutar este servicio localmente:
1.  Asegúrate de tener Docker y Docker Compose instalados.
=======
## Reverse Proxy

El Reverse Proxy actúa como punto de entrada unificado del sistema.
Redirige las peticiones a los microservicios correctos, maneja CORS y agrega una capa de seguridad adicional.

## Funcionalidades

Enrutamiento hacia los servicios internos

Balanceo de carga básico

Manejo de CORS y HTTPS

Logs de tráfico

## Tecnologías

NGINX o Express Gateway

## Estructura
reverse-proxy/
 ├── nginx.conf
 ├── Dockerfile
 └── README.md

## Ejecución
cd reverse-proxy
nginx -c ./nginx.conf

## Configuración ejemplo (nginx.conf)
location /api/auth/ {
    proxy_pass http://localhost:4000/;
}
location /api/posts/ {
    proxy_pass http://localhost:4001/;
}
location /api/email/ {
    proxy_pass http://localhost:4002/;
}

## Puertos por defecto
Servicio	Puerto
Auth Service	4000
Blog Service	4001
Email Service	4002
Frontend	5173
Reverse Proxy	8080
>>>>>>> 04553581254b252a953ff28ca76ac058dc7f2389
