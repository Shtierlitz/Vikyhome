# api/dump.py
# Файл нужный исключительно для создание файла данных переноса с локальной бд на боевую

import os
import django
from django.core.management import call_command

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
django.setup()

with open("db.json", "w", encoding='utf-8') as f:
    call_command('dumpdata', stdout=f)
