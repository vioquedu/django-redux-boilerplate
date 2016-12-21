# use base python image with python 3.5
FROM python:3.5

# add requirements.txt to the image
ADD requirements/development.txt /web_app/development.txt
ADD requirements/base.txt /web_app/base.txt

# set working directory to /web_app/
WORKDIR /web_app/

# install python dependencies
RUN pip install -r development.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' manager