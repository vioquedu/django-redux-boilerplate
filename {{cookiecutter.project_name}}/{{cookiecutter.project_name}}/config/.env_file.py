DEBUG=on
SECRET_KEY=CHANGE_ME!!!!
ALLOWED_HOSTS=,
DATABASE_URL=postgres://{{cookiecutter.db_user}}:{{cookiecutter.db_pwd}}@db/{{cookiecutter.db_name}}
EMAIL_HOST_USER={{cookiecutter.author_email}}
EMAIL_PWD=email_pwd 
EMAIL_ADMIN={{cookiecutter.author_email}}
