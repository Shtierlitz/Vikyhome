#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

domains=(vikyhome.com.ua www.vikyhome.com.ua)
data_path="./data/certbot"

# Путь к директории, где хранятся существующие сертификаты
existing_certs_path="./certs/"

echo "### Starting nginx ..."
docker-compose -f docker-compose.prod.yml up --force-recreate -d nginx
echo

echo "### Copying existing certificates for $domains ..."

# Создаем нужные директории
mkdir -p "$data_path/conf/live/$domains"

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  echo "### Downloading recommended TLS parameters ..."
  mkdir -p "$data_path/conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "$data_path/conf/ssl-dhparams.pem"
  echo
fi

# Копируем существующие сертификаты
cp ./certs/etc/letsencrypt/archive/vikyhome.com.ua/fullchain1.pem "$data_path/conf/live/$domains/fullchain.pem"
cp ./certs/etc/letsencrypt/archive/vikyhome.com.ua/privkey1.pem "$data_path/conf/live/$domains/privkey.pem"
cp ./certs/etc/letsencrypt/archive/vikyhome.com.ua/cert1.pem "$data_path/conf/live/$domains/cert.pem"
cp ./certs/etc/letsencrypt/archive/vikyhome.com.ua/chain1.pem "$data_path/conf/live/$domains/chain.pem"


echo "### Reloading nginx ..."
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload
