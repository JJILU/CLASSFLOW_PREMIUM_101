from flask import Blueprint,render_template


dash_bp = Blueprint("dash",__name__,template_folder="templates",static_folder="static")

from . import views

    


