# Django Celery Redis Rabbit SQLite Docker container
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMexsonFernandes%2FAsynchronous_Tasks-Django-Celery-RabbitMQ-Redis&count_bg=%2383DF3D&title_bg=%23000000&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 

Django Celery Redis Rabbit SQLite project skeleton

<a href='https://ko-fi.com/Y8Y31LBT4' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi3.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## Versions

App | Version
--- | ---
Python | 3.6
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
