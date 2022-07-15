#FROM python@sha256:1310efd0d9dd569e2857448c9803185e41c70ec741b3a24089d36cae8647fa14
# Build a "BaseImage" This is the first software our Docker has
FROM python:3.10

# Set environment variables
# 
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory (OPT is UIX Optional Folder where we  download and run allexternal or 3rd party applications, similar to program files on windows)
#
RUN mkdir -p /opt/services/djangomodels/src
WORKDIR /opt/services/djangomodels/src

# Copy the Python Library Names and versions of required foor our Application
#
COPY ./requirements.txt .

# install the specified libraries
#
RUN pip install --no-cache-dir -r requirements.txt

# The Project code is copied from the folder where this Dockerfile is located
#
COPY . /opt/services/djangomodels/src

# This Command Binds Django Appliation to Gunicorn Web Server
# 
CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "djangomodels.wsgi:application"]
