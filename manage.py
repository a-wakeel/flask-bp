"""
flask-bp module to manage database migrations.
"""
from flask_script import Manager  # pylint: disable=W0402
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
