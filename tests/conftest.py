"""
fixtures module
"""
import pytest

from testing.postgresql import Postgresql


# pylint: disable=redefined-outer-name, import-outside-toplevel

@pytest.yield_fixture(scope='session')
def app():
    """app fixture"""
    from app import app as app_
    app_.testing = True
    app_.debug = False

    # initialize a temp db instance
    postgresql = Postgresql()
    app_.config['SQLALCHEMY_DATABASE_URI'] = postgresql.url()
    yield app_

    postgresql.stop()


@pytest.fixture(scope='session')
def flask_app(app):
    """flask app fixture."""
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()
    yield client
    ctx.pop()


@pytest.yield_fixture(scope='session')
def db(app):
    """Database fixture"""
    from app import db

    # assign fixtured app
    db.app = app
    db.create_all()
    yield db

    db.drop_all()
