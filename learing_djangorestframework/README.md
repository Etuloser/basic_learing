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

## Tutorial 1: Serialization

[doc](https://www.django-rest-framework.org/tutorial/1-serialization/)

### Using ModelSerializers

```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
```

It's important to remember that `ModelSerializer` classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:

- An automatically determined set of fields.
- Simple default implementations for the `create()` and `update()` methods.

## Tutorial 2: Requests and Responses

[doc](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

### Requests objects

```python
# Only handles form data.  Only works for 'POST' method.
request.POST
 # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
request.data 
```

### Responses objects

```python
return Response(data)  # Renders to content type as requested by the client.
```

### Wrapping API views

1. The `@api_view` decorator for working with function based views.
2. The `APIView` class for working with class-based views.

## Tutorial 3: Class-based Views

[doc](https://www.django-rest-framework.org/tutorial/3-class-based-views/)

### Using generic class-based views

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

