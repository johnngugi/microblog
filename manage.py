from app import manager
from flask_migrate import upgrade
from app.models import Role, User


@manager.command
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()
    # create user roles
    Role.insert_roles()
    manager.run()
