# Makefile

run: 
	docker-compose up -d

stop:
	docker-compose down

data:
	docker-compose run web loaddata

test:
	docker-compose run web pytest
