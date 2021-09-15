
.PHONY: clean-pyc dist install-db start-dev test
.EXPORT_ALL_VARIABLES:
FLASK_ENV = development
FLASK_DEBUG = True
FLASK_APP = flask_bp.api

clean: clean-pyc
	rm	-rf dist .cache migrations drs.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name *pyc | grep __pycache__ | xargs rm -rf

start-dev:
	poetry install
	poetry run flask run -h 0.0.0.0 -p 5000

install-db:
	poetry run python3 manage.py db init
	poetry run python3 manage.py db migrate
	poetry run python3 manage.py db upgrade

upgrade-db:
	poetry run python3 manage.py db migrate
	poetry run python3 manage.py db upgrade

test:
	poetry install
	poetry run py.test --verbose

lint:
	poetry install
	poetry run pylint --verbose app/* tests/* manage.py
