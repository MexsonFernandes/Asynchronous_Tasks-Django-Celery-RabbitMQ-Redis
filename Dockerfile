# Use base python image with python 3.6
FROM python:3.6

# Install postgres client to check status of db cotainers
# This peace of script taken from Django's official repository
# It is deprecated in favor of the python repository
# https://hub.docker.com/_/django/
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
RUN mkdir /app
WORKDIR /app

# Add requirements.txt to the image
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy
COPY ./src /app

