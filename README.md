[![codecov](https://codecov.io/gh/a-wakeel/flask-bp/branch/master/graph/badge.svg)](https://codecov.io/gh/a-wakeel/flask-bp)
[![Build Status](https://travis-ci.com/a-wakeel/flask-bp.svg?branch=master)](https://travis-ci.com/a-wakeel/flask-bp)
![flask-bp](https://github.com/a-wakeel/flask-bp/workflows/flask-bp/badge.svg)

![header](/etc/images/header.png)

# flask-bp
**flask-bp** is a comprehensive flask boilerplate for prototyping. It includes most
common aspects of the projects such as Database migrations, resourceful routing, unit-testing
and many more.

## Features

### 1. Swagger API docs
Swagger docs are supported for API. [flask-apispec](https://github.com/jmcarp/flask-apispec) has been used to 
automatically generate swagger docs for APIs.
![Swagger Docs](/etc/images/apidocs-ss.png)

Swagger docs can be accessed at:
```http request
localhost:5000/apidocs
localhost:5000/apidocs-json
```

### 2. Automated Testing
Automated unit testing base is configured using [pytest](https://docs.pytest.org/en/latest/) with automatic
coverage report.
![Pytest](/etc/images/pytest.gif)

Tests can be engaged using:
```bash
make test
```

### 3. Automated Code Linter
Automated code linting is supported using [Pylint](https://www.pylint.org/)
![Pylint](/etc/images/pylint.gif)

Linter can be engaged using:
```bash
make lint
```

## Setup
A virtual environment should be used, e.g
```bash
virtualenv flaskbp-env
``` 
Activate the virtual environment and install the requirements:
```bash
source flaskbp-env/bin/activate
pip install -r requirements.txt
```
Run the flask-bp:
```bash
make start-dev
OR
flask run -h 0.0.0.0
```

## Setup Using Docker
Make sure you have installed docker and docker-compose.

- Create a `flaskbp` user with UID 9001 and change the ownership of the repo:
```bash
    sudo useradd -u 9001 -m -d /home/flaskbp -s /bin/bash flaskbp
    sudo chown -R 9001:9001 flask-bp
```

- Build Postgres Image using:
```bash
    make -f docker/postgres/Makefile
```

- Build the dev server image using:
```bash
    make -f docker/dev/Makefile
```

- After the build process completes, launch dev environment using:
```bash
    docker-compose -f docker/dev/devenv-with-local-db.yml run --rm --service-ports dev-shell
```

### Accessing flask-bp resources
To access the api server, you can access it on:
```bash
http://localhost:5000/api/v1/
```
There is one route defined which accepts a user information and return it back,
it can be accessed:
```bash
http://localhost:5000/api/v1/user
```
It supports GET & POST method, GET for getting the user information from the database and
POST to insert new user information to the database.

To access the auto generated swagger documentations:
```bash
http://localhost:5000/apidocs/
```

To export swagger docs in json format:
```bash
http://localhost:5000/apidocs-json/
```

### Database Migrations
To initialize  database migrations
```bash
make install-db
```

To upgrade database schema
```bash
make upgrade-db
```

### Others
To clean project
```bash
   make clean
```

To clean .pyc files
```bash
make clean-pyc
```

To run the tests
```bash
make test
```

## Open Source Resources Used
1. [Python](https://www.python.org/downloads/release/python-370/)
2. [Flask](https://github.com/pallets/flask)
3. [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)
4. [Flask-cors](https://github.com/corydolphin/flask-cors)
5. [Marshmallow Python](https://github.com/marshmallow-code/marshmallow)
6. [Flask SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)
7. [PyYAML](https://github.com/yaml/pyyaml)
8. [Flask Script](https://github.com/smurfix/flask-script)
9. [Flask Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
10. [apispec](https://github.com/marshmallow-code/apispec)
11. [flask-apispec](https://github.com/jmcarp/flask-apispec)
12. [testing.postgresql](https://github.com/tk0miya/testing.postgresql)
