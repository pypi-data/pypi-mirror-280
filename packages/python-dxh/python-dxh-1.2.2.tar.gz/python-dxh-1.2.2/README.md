![build](https://img.shields.io/github/workflow/status/iamfoysal/py-app-store/Build)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/iamfoysal/py-app-store/pulls)
[![PyPI](https://img.shields.io/pypi/v/python-app-store-scraper)](https://pypi.org/project/python-app-store-scraper/)
![downloads](https://img.shields.io/pypi/dm/python-app-store-scraper)
![license](https://img.shields.io/pypi/l/python-app-store-scraper)
![code style](https://img.shields.io/badge/code%20style-black-black)

`python-dxh` is a Python package designed to integrate with AWS services and Anticaptcha in Django projects. This package simplifies the configuration and usage of `AWS S3`, `AWS Textract`, and `Anticaptcha` by centralizing credential management in your Django settings.

## Installation

To install the `python-dxh` package, use pip:

```sh
pip install python-dxh
```
## Configuration

After installing the package, add AWS and Anticaptcha credentials to the Django project's settings.py file. This ensures that the necessary credentials are available for the package to interact with the services

## AWS S3 Configuration
Add the following variables to your settings.py file:
```python
DJANGO_AWS_S3_REGION_NAME = '<your-aws-s3-region-name>'
DJANGO_AWS_ACCESS_KEY_ID = '<your-aws-access-key-id>'
DJANGO_AWS_SECRET_ACCESS_KEY = '<your-aws-secret-access-key>'
DJANGO_AWS_STORAGE_BUCKET_NAME = '<your-aws-storage-bucket-name>'
DJANGO_AWS_TEXTRACT_REGION_NAME = '<your-aws-textract-region-name>'
```

## Anticaptcha Configuration
Add the following variable to your `settings.py` file:

```python
ANTICAPTCHA_API_KEY = '<your-anticaptcha-api-key>'
```

## Usage
Once the settings are configured, the package can be used in the Django project as follows:
    
```python   
from python_dxh.aws.s3_client import S3Client
from python_dxh.aws.textract import textract_handler
from python_dxh.anticaptcha.captcha import AntiCaptchaSolver
```
```python
from python_dxh.s3_client import S3Client

# Initialize the S3 client
s3_client = S3Client()

# Upload a file to S3
s3_client.upload_to_s3('path/to/local/file', 's3/object/name')

# Delete an object from S3
s3_client.delete_from_s3(object_key='s3/object/name')
```

## Auditlog Configuration
To enable audit logging, include auditlog in INSTALLED_APPS and configure the AuditActorMiddleware.

Add auditlog to INSTALLED_APPS in settings.py:

```
INSTALLED_APPS = [
    ...
    'auditlog',
    ...
]
```

Add AuditActorMiddleware to MIDDLEWARE in settings.py:

```python
MIDDLEWARE = [
    ...
    'python_dxh.middleware.AuditActorMiddleware',
    ...
]
``` 

## Websocket Configuration

This middleware for JWT authentication in WebSocket connections.

Checks the 'authorization' header for a JWT token, retrieves the corresponding user,
and adds the user to the connection scope.

If the token is invalid or not provided, sets the user to AnonymousUser.

```python
from python_dxh.middleware import JwtAuthMiddleware


'websocket': JwtAuthMiddleware(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    )
``` 