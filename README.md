# Django Celery Redis Rabbit SQLite Docker container

Django Celery Redis Rabbit SQLite project skeleton

## Versions

App | Version
--- | ---
Python | 3.7
Django | 2.1
Celery | 4.1.0
Redis | 2.1
Rabbit | 3.7.8

## What is included

- Redis as a result backend
- RabbitMQ as a message broker
- pgAdmin to view the database schema
- Scalable Docker and Docker Compose configuration (HAProxy)
- Email support when job submitted (added in task file)

## Docker Compose containers

- redis (Redis result backend for Celery)
- rabbit (RabbitMQ message broker for Celery)
- web (Django application)
- worker (Celery worker)
- lb (HAProxy load balancer)

# Project structure

    django-celery-skeleton/
    |---src                                     # django project folder
    |   |---dcs                                 # django root configuration
    |   |   |---settings.py
    |   |   |---urls.py
    |   |   |---wsgi.py
    |   |   |---celeryconf.py
    |   |---files
    |   |   |---tempaltes                       # view templates
    |   |   |   |---index.html
    |   |   |---media                           # images, sized cache and placeholder
    |   |   |   |---.gitignore
    |   |   |   |---placeholder.png
    |   |   |   |---README.md
    |   |   |---static
    |   |   |   |---placeholder.png
    |   |   |---README.md
    |   |---manage.py
    |---.gitignore
    |---.dockerignore
    |---Vagrantfile
    |---Dockerfile
    |---docker-compose.yml
    |---requirements.txt
    |---README.md

# Setup & Run

## Copy git repository

    git clone https://github.com/
    cd

## Email settings
    # add the following info in src/dcs/settings.py
    EMAIL_HOST_USER = 'user@gmail.com'
    EMAIL_HOST_PASSWORD = 'XXXXXXXXXX'

## Run inside docker

    # build docker containers
    docker-compose build

    # option 1: run 1 instance of web
    docker-compose up

    # option 2: run 3 instances of web over load balancer
    docker-compose up --scale web=3

    # option 3: run in background with -d
    docker-compose up -d --scale web=3

You can also run manage.py commands using docker environment, for example tests.

    docker-compose run web python ./manage.py test

See docker's logs

    docker-compose logs --tail 5

## Run from local machine

    # Install requirements
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

    # Move to 'src' folder
    cd src

    # Run worker
    celery worker -A dcs.celeryconf -Q default -n default@%h

    # Start application on another console
    python manage.py runserver

## Credits
   # Django Celery Skeleton (updated the repository with email support and pgAdmin container)
   <a href="https://github.com/KenanBek/django-celery-skeleton">Django Celery Skeleton</a>
