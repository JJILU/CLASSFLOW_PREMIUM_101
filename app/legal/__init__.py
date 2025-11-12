from flask import Blueprint

legal_bp = Blueprint("legal",__name__,template_folder="templates",static_folder="static",static_url_path='/auth_static')

from . import views