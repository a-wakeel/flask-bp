"""
Schemas for user models.
"""
from marshmallow import fields, Schema


class UserResponse(Schema):
    """Response schema for user model."""
    full_name = fields.String(required=True)
    user_name = fields.String(required=True)
    email_id = fields.String(required=True)


class GetUserArgs(Schema):
    """Request schema for get user route."""
    user_id = fields.Integer(required=True)

    @property
    def fields_dict(self):
        """Convert declared fields to dictionary."""
        return self._declared_fields


class SuccessResponse(Schema):
    """Success or error response schema."""
    message = fields.String(required=True)


class UserArgs(Schema):
    """Request/Args schema for user model."""
    full_name = fields.String(required=True)
    user_name = fields.String(required=True)
    email_id = fields.Email(required=True)

    @property
    def fields_dict(self):
        """Convert declared fields to dictionary."""
        return self._declared_fields
