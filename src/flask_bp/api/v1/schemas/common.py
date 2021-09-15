"""
Schemas for common routes.
"""
from marshmallow import fields, Schema


class CommonResponse(Schema):
    """Schema for the common response route."""
    message = fields.String(required=True)
    method = fields.String(required=True)
    route_path = fields.String(required=True)
