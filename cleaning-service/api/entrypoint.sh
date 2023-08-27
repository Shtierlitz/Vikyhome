#!/bin/bash

echo "Waiting 10 seconds before proceeding"
sleep 3
if [ "$DATABASE" = "postgres" ]; then
  echo "Waiting for postgres..."

  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

echo "Start migration"


python manage.py migrate

echo "Migration done!"

# Создаем суперпользователя, если он еще не создан.
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(os.environ.get('DJANGO_SUPERUSER_NAME_M'), os.environ.get('DJANGO_SUPERUSER_EMAIL_M'), os.environ.get('DJANGO_SUPERUSER_PASSWORD_M')) if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_NAME_M')).exists() else None" | python manage.py shell
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(os.environ.get('DJANGO_SUPERUSER_NAME_W'), os.environ.get('DJANGO_SUPERUSER_EMAIL_W'), os.environ.get('DJANGO_SUPERUSER_PASSWORD_W')) if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_NAME_W')).exists() else None" | python manage.py shell
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(os.environ.get('DJANGO_SUPERUSER_NAME_OWNER'), os.environ.get('DJANGO_SUPERUSER_EMAIL_OWNER'), os.environ.get('DJANGO_SUPERUSER_PASSWORD_OWNER')) if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_NAME_OWNER')).exists() else None" | python manage.py shell

echo "Superuser is created!"

python manage.py loaddata db.json

echo "Data added to database!"

exec "$@"
