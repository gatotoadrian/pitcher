# from multiprocessing import managers
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager, Server

from app import create_app, db
from app.models import  User,Pitch

#Creating app instance
app = create_app('production')
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command('db', MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app=app, db = db, User = User, Pitch=Pitch )


if __name__ == '__main__':
    manager.run()
