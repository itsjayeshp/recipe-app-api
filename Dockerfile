#this Dockerfile uses an official Python runtime as a parent image

FROM python:3.9-alpine3.13 

#LABEL description="This is a Dockerfile for Recipe App API"
LABEL maintainer="jayesh.com"
# Set environment variables
ENV PYTHONUNBUFFERED 1 
#to ensure that the Python output is sent straight to terminal (e.g., your container log) without being buffered
ENV PYTHONDONTWRITEBYTECODE 1 
#to prevent Python from writing .pyc

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./app /app

WORKDIR /app
EXPOSE 8000

# Build argument to specify development mode
ARG DEV=false 

# Create a virtual environment and install dependencies
# Use a virtual environment to isolate dependencies
# Create a non-root user to run the application
# Switch to the non-root user
# Final stage: set up the application
# Upgrade pip to the latest version line 2
#for PostgreSQL database client this will help to connect to PostgreSQL database line 3
# temporary build dependencies for compiling packages. why because some packages have C extensions that need to be compiled during installation line 4
# Install production dependencies from requirements.txt line 5
# this line is for temporary build dependencies musl-dev is for C standard library
# this line is for development dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \ 
    apk add --update --no-cache postgresql-client && \ 
    apk add --update --no-cache --virtual .tmp-build-deps \ 
        build-base postgresql-dev musl-dev && \ 
    /py/bin/pip install -r /tmp/requirements.txt && \ 
    if [ "$DEV" = "true" ] ; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user


# Update PATH environment variable
ENV PATH="/py/bin:$PATH"

USER django-user


