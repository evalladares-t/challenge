# Challenge Backend Api Django

Este proyecto es un ejemplo de cómo levantar una aplicación utilizando Docker Compose.

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener lo siguiente instalado en tu sistema:

- Docker
- Docker Compose
- Postman (opcional)

## Ejecución del proyecto

Para ejecutar el proyecto, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local: `git clone https://github.com/evalladares-t/challenge.git`.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el siguiente comando para levantar la aplicación y la base de datos: `docker-compose up -d --build`.
4. Se deberá correr las migraciones para llenar las tablas en la base de datos: `docker-compose exec web python manage.py migrate --noinput`.
5. Una vez que se haya completado la ejecución, abre tu navegador web y visita `http://localhost:8000`.

## Documentación de endpoints

Los endpoints de este proyecto están documentados en Postman. Puedes importar el archivo `postman_collection.json` a tu aplicación de Postman para ver la documentación completa de los endpoints.

Para usar los endpoints, utiliza la URL `http://localhost:5000` en lugar de la URL base que se proporciona en la documentación de Postman.

## Créditos

Este proyecto fue creado por `Edward Valladares` para un ejemplo de un proyecto sencillo utilizando Docker Compose.

