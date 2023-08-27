# Vikyhome cleaning-service API

## Description
DRF + React project (cleaning website)

## Technologies used
`Django`, `Django Rest Framework`,  `Docker`,  `PostgreSQL`, `Nginx`, `Swagger-ui drf_yasg`, `JWT`, `cloudinary`, `unittest`



## Getting started

To make it easy for you to get started with Cleaning-service, 
here's a list of recommended next steps.

## Download
Download the repository with this command: 
```bash
git clone https://github.com/Shtierlitz/Cleaning-cervice.git
```

## Create Files
For the local server to work correctly, create your own file `local_settings.py` 
and place it in a folder next to the file `settings.py` of this Django project.
You will also need to create `.env` file and place it in the root of the project.

### Required contents of the local_settings.py file:
```python  
# api/api/local_settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
```

### Required contents of the .env file:
```python
SECRET_KEY='<your SECRET key>'   

DATABASE_NAME="<database name>"  
DATABASE_USER="<database username>"  
DATABASE_PASS="<database password>"  
DATABASE_HOST="pg_db"  
DATABASE_PORT="5432"

DJANGO_SUPERUSER_NAME_M="<male superuser name>"
DJANGO_SUPERUSER_PASSWORD_M="<male superuser password>"
DJANGO_SUPERUSER_EMAIL_M="<male superuser email>"

DJANGO_SUPERUSER_NAME_W="<female superuser name>"
DJANGO_SUPERUSER_PASSWORD_W="<female superuser password>"
DJANGO_SUPERUSER_EMAIL_W="<female superuser email>"

DJANGO_SUPERUSER_NAME_OWNER="<owner superuser name>"
DJANGO_SUPERUSER_PASSWORD_OWNER="<owner superuser password>"
DJANGO_SUPERUSER_EMAIL_OWNER="<owner superuser email>"

CLOUD_NAME="<cloudinary cloud name>"
API_KEY="<cloudinary api key>"
API_SECRET="<cloudinary api secret key>"

IP_ES2="<IP address of your deploy instance>"
```

# Localhost development

## Django run
To run localhost server just get to the folder where `manage.py` is and then run the command:
```bash
python manage.py runserver
```
## Test 

To run tests from the localhost, type in the folder next to the file `manage.py`:  
```bash
python manage.py test 
````

## Docker localhost
To use docker in localhost you need to have `local_settings.py` behind yours `settings.py` file.
```bash
docker-compose -f docker-compose.yml up -d --build

````

## Docker deploy
Find server and create an instance.  
Run next commands:  
```bash
sudo apt-get update  
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
sudo apt-get update  
sudo apt-get install docker-ce  
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)"  
sudo chmod +x /usr/local/bin/docker-compose  
docker --version  
```

### Now clone repository:
```bash
sudo git clone https://github.com/Shtierlitz/Cleaning-cervice.git
```

### Dont forget to create `.env` file
### Now you can run Docker container in your server machine:
```bash
docker-compose -f docker-compose.yml up -d --build
```

## Api 
To get excess to `API` if you want to use `Postman` 
you need to generate and verify `token`. It is possible after you register in website

`../api/v1/token/` - obtain token  
`../api/v1/token/verify/` - verify your token  
`../api/v1/token/refresh/` - refresh token if it has expired

### You can follow the following paths to use the `API`:

GET /api/v1/services/ - get list of all services
POST /api/v1/services/ - create new service
GET /api/v1/services/{id}/ - get details of current service
PUT /api/v1/services/{id}/ - update details of current service
DELETE /api/v1/services/{id}/ - delete current service

GET /api/v1/extra/ - get list of all extras
POST /api/v1/extra/ - create new extra
GET /api/v1/extra/{id}/ - get details of current extra
PUT /api/v1/extra/{id}/ - update details of current extra
DELETE /api/v1/extra/{id}/ - delete current extra

swagger/ - swagger-ui page
redoc/ - swagger-redoc page

# Sources
Django Rest Framework https://www.django-rest-framework.org/  
Swagger https://habr.com/ru/companies/otus/articles/583220/  
JWT https://django-rest-framework-simplejwt.readthedocs.io/en/latest/  
Docker https://docs.docker.com/  

