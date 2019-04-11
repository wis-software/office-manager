# About project
The backend for internal company's CRM using Python, Django and GraphQL.

Anyone can take part in the development provided abidance with the contribution rules.

**Pay attention: Any commercial task has more priority.**

## Table of contents

1. [Getting started](#getting-started)
2. [Contribution rules](#contribution-rules)
3. [Workflow](#workflow)
4. [Notes](#notes)

## Getting Started

You can use [Docker](docker/README.md) to install and run the project.

Or you can install it manually:

**Requirements**
* Python 3.7
* Virtualenv
* Docker 

1. Clone repository `git clone https://github.com/wis-software/office-manager.git`
2. Create virtualenv in directory where repository is located `virtualenv -p python3 office-manager-env`
3. Run container with PostgreSQL 10 and create DB: <br>
    `$ docker run --name postgres -e POSTGRES_PASSWORD=secret -v $(pwd)/postgres:/var/lib/postgresql/data -p 54321:5432 -d postgres:10`<br>
    `$ docker run -it --rm --link postgres:postgres -e PGPASSWORD=secret postgres:10 createdb -h postgres -U postgres office_manager`
4. Go to the project's root
5. Rename **.env.example**  to **.env**
6. Change in **.env**:<br>
    `ALLOWED_HOSTS=' '` to `ALLOWED_HOSTS=127.0.0.1`<br>
    `POSTGRES_HOST=database` to `POSTGRES_HOST=127.0.0.1`<br>
    `POSTGRES_PORT=5432` to `POSTGRES_PORT=54321`<br>
    `POSTGRES_USER=office_manager_user` to `POSTGRES_USER=postgres`<br>
    `POSTGRES_PASSWORD=5e4d3c2b` to `POSTGRES_PASSWORD=secret`
7. Activate virtualenv `source ../office-manager-env/bin/activate` (when you don't need the activated environment you can turn off it with command `deactivate` ) 
8. Run migrations `env PYTHONPATH=$(pwd)/src python src/manage.py migrate`
9. Create superuser `env PYTHONPATH=$(pwd)/src python src/manage.py migrate`
10. Run server `env PYTHONPATH=$(pwd)/src python src/manage.py runserver 0.0.0.0:8001`
11. Open `http://127.0.0.1:8001/admin/`

### Contribution rules
1. Follow [PEP8](https://www.python.org/dev/peps/pep-0008/)
2. All comments and tasks names have to be in english!
3. Every module have to be covered by tests at least 80%
4. Every task should be done in separate branch
5. You need to create the PR for the completed task. PR can be merged only after ALL successfully passed tests.

### Workflow

1. Choose the task from TODO list, reference to yourself and move the task to the **In progress** column
2. Create a new branch from master
3. Complete the task, write tests
4. Create the PR, add colleague as reviewer
5. Move the card task to the **Testing** column
6. Take care of task testing after deploy to staging to move the task to the **Done** column

### Notes

To run tests for all project you need to run following command in project dictionary:

`python manage.py test`

For specific application:

`python manage.py test your_app`
