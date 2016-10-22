# Django redux boilerplate

## Django

Django is used for the backend along with the following packages:

* dj-database-url
* django-environ
* djangorestframework
* djangorestframework-jwt
* dealer
* django-webpack-loader

### Installation

1. Install requirements:

	``pip install -r requirements/development.txt``

2. Define a `env_file.py` in the inside the `config` folder.

## React-Redux

The frontend application is set up with react-redux. It includes
jwt authentication.

1. Install dependencies

	``npm install``

2. Use node to serve frontend application:

	``npm run start``

### Install bower components

    ``bower install``