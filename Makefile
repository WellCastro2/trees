# Makefile

build:
	docker-compose build && docker-compose up db &

run:
	docker-compose up &

super:
	docker-compose run web python manage.py createsuperuser

stop:
	docker-compose down

test:
	docker-compose run web pytest

