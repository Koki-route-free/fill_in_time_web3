python 3.9
django 4.0
bootstrap -v 4

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
  docker compose run --rm web python manage.py makemigrations [app_name]

migrate:
  docker compose run --rm web python manage.py migrate

createsuperuser:
  docker compose run --rm web python manage.py createsuperuser

