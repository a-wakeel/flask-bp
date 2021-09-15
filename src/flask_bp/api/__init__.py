"""
Top level module of the flask-bp api.
"""
from datetime import datetime

from flask import Flask
from flask_cors import CORS
import yaml
from flask_sqlalchemy import SQLAlchemy

from flask_bp.api.common.swagger_docs import SwaggerDocs

# import strptime to avoid weird issues described @ http://bugs.python.org/msg221094
datetime.strptime('', '')


def create_app():
    """Factory method to create api instance."""
    # Create WSGI api instance - this __name__.split('.') handles
    # the case where the file is part of a package.
    app_ = Flask(__name__.split('.')[0])

    # to allow cross domain resource sharing over all domains,
    # for more specific usage see @ https://github.com/corydolphin/flask-cors
    CORS(app_)

    # load the configuration file
    try:
        app_config = yaml.safe_load(open('etc/config.yml'))
    except yaml.YAMLError as e:  # exceptions can be specific to the possible errors
        app_.logger.error('exception encountered while parsing the configuration file, check the logs')
        app_.logger.exception(e)
        sys.exit(1)

    # when the file is loaded properly, load & set database configs for sqlalchemy
    database_host = app_config['database']['host']
    database_port = app_config['database']['port']
    database_user = app_config['database']['user_name']
    database_password = app_config['database']['password']
    database_name = app_config['database']['database_name']

    # setup database uri
    # i used postgres as example database however any database can be used which is supported be sqlalchemy
    app_.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://%s:%s@%s:%s/%s' % \
                                             (database_user, database_password, database_host,
                                              database_port, database_name)
    # to suppress the track modification overhead warning and set it off
    app_.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app_


app = create_app()


@app.after_request
def add_no_cache(response):
    """Make sure no API responses are cached by setting headers on the response."""
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.cache_control.max_age = 0
    response.headers['Pragma'] = 'no-cache'
    response.expires = 0
    return response


@app.after_request
def add_security_headers(response):
    """Makes sure appropriate security headers are added for each API."""
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


db = SQLAlchemy(session_options={'autocommit': False})
db.init_app(app)
# import all the defined routes here
from src.flask_bp.api import *  # pylint: disable=wrong-import-position
