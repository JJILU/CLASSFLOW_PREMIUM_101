from flask import Flask 
from .extensions import login_manager,db,migrate



def create_app():
    
    app = Flask(__name__)

    # setup app configurations

    # init extensions

    # import models 

    # import & register blueprints
    from app.dasboard.views import dash_bp

    app.register_blueprint(dash_bp, url_prefix="/")



    return app