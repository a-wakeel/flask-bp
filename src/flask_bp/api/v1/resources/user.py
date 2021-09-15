"""
Module for user resource.
"""
import json

from flask import Response
from flask_apispec import marshal_with, doc, MethodResource, use_kwargs

from flask_bp.api.database import User
from flask_bp.api.v1 import UserArgs, UserResponse, GetUserArgs, SuccessResponse


class Users(MethodResource):
    """Class for handling user resources."""

    @doc(description='To get user info from database', tags=['Users'])
    @marshal_with(UserResponse, code=200, description='user info found (success)')
    @use_kwargs(GetUserArgs().fields_dict, locations=['query'])
    def get(self, **kwargs):
        """GET method handler."""
        user_id = kwargs.get('user_id')
        user = User()
        return Response(json.dumps(UserResponse().dump(user.get(user_id)).data),
                        status=200, mimetype='application/json')

    @doc(description='To add a user into the database', tags=['Users'])
    @marshal_with(UserResponse, code=200, description='On success')
    @marshal_with(SuccessResponse, code=500, description='On error')
    @use_kwargs(UserArgs().fields_dict, locations=['json'])
    def post(self, **kwargs):
        """POST method handler."""
        user_data = kwargs
        user = User(full_name=user_data.get('full_name'),
                    user_name=user_data.get('user_name'),
                    email_id=user_data.get('email_id'))
        user.add()
        return Response(json.dumps({'message': 'user {0} added successfully'.format(user_data.get('user_name'))}),
                        status=200, mimetype='application/json')
