"""
Module for common resources.
"""
import json

from flask import Response
from flask_apispec import MethodResource

from flask_bp.api import CommonResponse


class BaseRoutes(MethodResource):
    """Base Routes Handlers class."""

    # noinspection PyMethodMayBeStatic
    def get(self):
        """GET method handler for base routes."""
        # your code here
        return Response(json.dumps(CommonResponse().dump({'message': 'flask-bp API Version 1.0',
                                                          'method': 'GET',
                                                          'route_path': 'api/v1/'})),
                        status=200, mimetype='application/json')

    # noinspection PyMethodMayBeStatic
    def post(self):
        """POST method handler for base routes."""
        # your code here
        return Response(json.dumps(CommonResponse().dump({'message': 'flask-bp API Version 1.0',
                                                          'method': 'POST',
                                                          'route_path': 'api/v1/'}).data),
                        status=200, mimetype='application/json')

    # noinspection PyMethodMayBeStatic
    def put(self):
        """PUT method handler for base routes."""
        # your code here
        return Response(json.dumps(CommonResponse().dump({'message': 'flask-bp API Version 1.0',
                                                          'method': 'PUT',
                                                          'route_path': 'api/v1/'}).data),
                        status=200, mimetype='application/json')
