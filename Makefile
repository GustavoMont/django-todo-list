up:
	docker-compose up
down:
	docker-compose down
setup:
	docker-compose exec web python manage.py migrate
show-db:
	docker-compose exec db bash 