import os
import sys

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from configs.postgres import DB
from configs.redis import RedisWorker, RedisServer
from models import *
from routes.index import index_blueprint


def create_app():
    """
    Server, Postgres, Redis
    """
    server = Flask(__name__)
    load_dotenv()
    server.config.from_object(
        "configs.config." + str(os.getenv("PYTHON_ENV")) + "Config"
    )
    DB.init_app(server)
    return server


# Initialize application server
app = create_app()
# Register blueprint
app.register_blueprint(index_blueprint)

# Define migration folder
MIGRATION_DIR = os.path.join("migrations")
migrate = Migrate(app, DB, directory=MIGRATION_DIR)
manager = Manager(app)

# Add commands into manager
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(port=os.getenv("PORT"), host=os.getenv("HOST")))
manager.add_command("redis-worker", RedisWorker())
manager.add_command("redis-server", RedisServer())

if __name__ == "__main__":
    manager.run()
