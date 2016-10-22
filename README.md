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
1. Clone repository using cookiecutter
   	 
	 ``cookiecutter https://github.com/vioquedu/django-redux-boilerplate.git``

2. Install requirements:

	``pip install -r requirements/development.txt``

2. Create a `env_file.py` inside the `config` folder which should look like this:

   ```
   DEBUG=on
   SECRET_KEY=CHANGE_ME!!!!!
   DATABASE_URL=connection_to_database
   ALLOWED_HOSTS=example.com,www.example.com
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_PWD=your_pwd
   EMAIL_ADMIN=admin1@example.com,admin2@example.com
   ```

3. Create initial tables in database running:

   ``python manage.py migrate``

4. Create a super user

   ``python manage.py createsuperuser``

5. Start a development server

   ``python manage.py runserver``

## React-Redux

The frontend application is set up with react-redux. It includes
jwt authentication.

1. Install dependencies

	``npm install``

2. Use node to serve frontend application:

	``npm run watch``

### Install bower components

	``bower install``

