# AlphaBackend

Este es el repositorio de AlphaSolutions para el proyecto del curso IIC3143 - Desarrollo de Software. Esta utiliza docker, django, ninja api y postgresql.

## Setup & Run
1) build the app

`docker-compose build`

2) migrate models into db

`docker-compose run web python manage.py migrate`

3) run the app

`docker-compose up`
