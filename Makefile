# Makefile

build:
	docker-compose build

run: 
	docker-compose up -d

stop:
	docker-compose down

data:
	docker-compose run web python manage.py loaddata core/dump/db.json

test:
	docker-compose run web pytest

