"""
User model for user table in database.
"""
from src.flask_bp.api import db, app


class User(db.Model):
    """Class for maintaining user table in the database."""
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(24), nullable=False)
    email_id = db.Column(db.String(120), nullable=False)

    def __init__(self, full_name=None, user_name=None, email_id=None):
        """Constructor."""
        self.full_name = full_name
        self.user_name = user_name
        self.email_id = email_id

    def add(self):
        """Method to insert user details into the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error('An exception encountered while inserting user record into the database')
            app.logger.exception(e)
            raise e

    def get(self, user_id):
        """Method to return a user info from database."""
        return self.query.filter_by(id=user_id).first()
