最初
docker compose run --rm web django-admin startproject fill_in_time .




変更時
docker compose up -d --build
docker compose restart

通常時
docker compose up -d(backend)
作成時
docker compose up -d --build

止め方
docker compose down
停止と消し方
docker compose down -v

makemigrations:
  docker compose run --rm web python manage.py makemigrations

migrate:
  docker compose run --rm web python manage.py migrate

createsuperuser:
  docker compose run --rm web python manage.py createsuperuser

python 3.9
bootstrap -v 5