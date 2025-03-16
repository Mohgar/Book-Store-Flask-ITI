from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager



bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()






def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(Config.get(environment or "development"))

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from .models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.main.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth.routes import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app import models

    return app