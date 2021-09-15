"""
Module for swagger docs implementation.
"""
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


class SwaggerDocs:
    """Class for swagger api docs."""

    def __init__(self, app, version):
        """Constructor."""
        self.app = app
        self.title = 'flask-bp'
        self.version = version
        self.plugins = [MarshmallowPlugin()]
        self.swagger_json_url = '/apidocs-json/'
        self.swagger_url = '/apidocs/'

    def init_docs(self):
        """method to bind docs with api instance."""
        self.app.config.update({
            'APISPEC_SPEC': APISpec(
                title=self.title,
                version=self.version,
                info={'description': self.spec_description()},
                plugins=self.plugins,
                openapi_version='2.0'
            ),
            'APISPEC_SWAGGER_URL': self.swagger_json_url,
            'APISPEC_SWAGGER_UI_URL': self.swagger_url,
        })
        return FlaskApiSpec(self.app)

    def spec_description(self):
        """Generate description."""
        return 'flask-bp swagger docs.'
