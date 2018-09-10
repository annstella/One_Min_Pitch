from app import create_app,db
from flask_script import Manager,Server
from app.models import Group
from flask_migrate import Migrate,MigrateCommand

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)