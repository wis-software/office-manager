## Overview
Here are the Dockerfile and assets related to it to run the project in a Docker container.

## Requirements
* Docker
* Docker-compose

## Getting Started

1. Rename **.env.example** into **.env**.
2. Change `ALLOWED_HOSTS=''` to `ALLOWED_HOSTS=127.0.0.1` in **.env**
3. Run `docker-compose up`
4. Create superuser with `docker exec -it officemanager_web_1 python3 manage.py createsuperuser`
5. Open `http://127.0.0.1/admin/` to be sure that everything works


## Deleting project
If you need to delete the project (for example, to install it again) you need to do the following:
1. Stop and remove all project containters with `docker-compose down` in project's root directory
2. Delete directory **dbdata**
3. Delete all the Docker images related to the project by invoking `docker rmi officemanager_web postgres python:3.5 redis`
