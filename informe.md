# Informe de Despliegue y Monitoreo

## Plataforma de despliegue:
Se utilizó **Render.com**, un servicio PaaS gratuito, para alojar una aplicación básica construida con Flask.

## Configuración:
- El código fue subido a GitHub.
- Se utilizó un archivo `render.yaml` para automatizar el despliegue.
- La aplicación incluye un endpoint `/status` para facilitar el monitoreo.

## Monitoreo:
Se configuró un monitor HTTP con **UptimeRobot** apuntando al endpoint `/status`. Las métricas que se revisan son:

- **Uptime** (disponibilidad del endpoint)
- **Tiempo de respuesta**
- **Logs de fallos (en caso de que no se reciba respuesta 200)**

Esto permite garantizar que la aplicación esté disponible 24/7 y recibir alertas si se detecta alguna interrupción.

## URL pública:
[https://flask-app-example.onrender.com](https://flask-app-example.onrender.com)