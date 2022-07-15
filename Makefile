build:
	docker build --tag word-counter .

start:
	docker run --publish 8000:8000 word-counter

test:
	docker run word-counter sh -c "python manage.py test"