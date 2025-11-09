from flask import Flask 
from .extensions import login_manager,db,migrate
from config import Config

print(Config.SQLALCHEMY_DATABASE_URI)


def create_app():
    
    app = Flask(__name__)

    # setup app configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI

    # init extensions
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    

    # import models
    from app.auth.models import TeacherSchoolRecord,StudentSchoolRecord,Teacher,Admin,Student

    # load user
    @login_manager.user_loader
    def load_user(user_id):
        # Example user_id: "Admin:3"
        model_name, pk = user_id.split(":", 1)  # Split into ["Admin", "3"]
        pk = int(pk)

        if model_name == "Teacher":
            return Teacher.query.get(pk)
        if model_name == "Admin":
            return Admin.query.get(pk)
        if model_name == "Student":
            return Student.query.get(pk)
        return None 

    # import & register blueprints
    from app.dash.views import dash_bp
    from app.auth.views import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(dash_bp, url_prefix="/dash")






    return app