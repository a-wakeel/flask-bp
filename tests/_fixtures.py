"""
fixtures module
"""
import pytest

from testing.postgresql import Postgresql


# pylint: disable=redefined-outer-name, import-outside-toplevel

@pytest.yield_fixture(scope='session')
def app():
    """api fixture"""
    from flask_bp.api import app as app_
    app_.testing = True
    app_.debug = False

    # initialize a temp db instance
    postgresql = Postgresql()
    app_.config['SQLALCHEMY_DATABASE_URI'] = postgresql.url()
    yield app_

    postgresql.stop()


@pytest.fixture(scope='session')
def flask_app(app):
    """flask api fixture."""
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()
    yield client
    ctx.pop()


@pytest.yield_fixture(scope='session')
def db(app):
    """Database fixture"""
    from flask_bp.api import db

    # assign fixtured api
    db.app = app
    db.create_all()
    yield db

    db.drop_all()
