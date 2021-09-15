"""
Top level modules for the routes of flask-bp api version 1.0 routes.
"""
from flask_restful import Api

from flask_bp.api import app
from flask_bp.api.v1.resources import BaseRoutes
from flask_bp.api import Users

# initialize flask-restful api instance
# for more details see @ https://flask-restful.readthedocs.io/en/latest/
api = Api(app, prefix='/api/v1')

# add a resource
# noinspection PyTypeChecker
api.add_resource(BaseRoutes, '/')
api.add_resource(Users, '/user')
