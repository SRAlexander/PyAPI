# Use the Python3.7.2 image
FROM python:3.7.2-stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev \
    gcc \
    g++ \
    build-essential

# Required for Synapse access 
RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get install apt-transport-https
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --force-yes --allow-unauthenticated --no-install-recommends \
    msodbcsql17

RUN apt-get install openssh-client \
    && echo "root:Docker!" | chpasswd

COPY sshd_config /etc/ssh/

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /service
ADD ./service /app

# Configurable arguments with defaults
ARG BUILDENV=dev
ARG fileCommand="app-${BUILDENV}:app"

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install Cython numpy
RUN pip install -r requirements.txt

EXPOSE 80 2222

# run the command to start uWSGI
ENV fileCommand ${fileCommand}
CMD gunicorn --workers 4 --bind 0.0.0.0:80 ${fileCommand}