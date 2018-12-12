[![codecov](https://codecov.io/gh/a-wakeel/flask-bp/branch/master/graph/badge.svg)](https://codecov.io/gh/a-wakeel/flask-bp)
[![Build Status](https://travis-ci.com/a-wakeel/flask-bp.svg?branch=master)](https://travis-ci.com/a-wakeel/flask-bp)



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
1. [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. [Flask 1.0.2](https://github.com/pallets/flask)
3. [Flask-Restful 0.3.6](https://flask-restful.readthedocs.io/en/latest/)
4. [Flask-cors 3.0.6](https://github.com/corydolphin/flask-cors)
5. [Marshmallow Python 2.16.1](https://github.com/marshmallow-code/marshmallow)
6. [Flask SQLAlchemy 2.3.2](https://github.com/mitsuhiko/flask-sqlalchemy)
7. [PyYAML 3.13](https://github.com/yaml/pyyaml)
8. [Flask Script 2.0.6 (deprecated)](https://github.com/smurfix/flask-script)
9. [Flask Migrate 2.3.0](https://github.com/miguelgrinberg/Flask-Migrate)
10. [apispec 0.39.0](https://github.com/marshmallow-code/apispec)
11. [flask-apispec 0.7.0](https://github.com/jmcarp/flask-apispec)
12. [testing.postgresql](https://github.com/tk0miya/testing.postgresql)
