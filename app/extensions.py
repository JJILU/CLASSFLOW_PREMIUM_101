from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from faker import Faker


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
faker = Faker()