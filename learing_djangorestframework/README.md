# README

> Library reference
>
> [HomePage](https://www.django-rest-framework.org/)
>
> [QuickStart](https://www.django-rest-framework.org/tutorial/quickstart/)

## Project setup

```shell
# Create the project directory
$ mkdir tutorial
$ cd tutorial

# Create a virtualenv to isolate our package dependencies locally
$ virtualenv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtualenv
$ pip install django
$ pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
$ cd tutorial
django-admin startapp quickstart
$ cd ..

# Sync database for the first time
$ python manage.py migrate
# Create superuser
$ python manage.py createsuperuser --email admin@example.com --username admin
```

