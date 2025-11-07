from . import auth_bp
from flask import render_template



@auth_bp.route("/")
def register_or_login():
    return render_template("auth/index.html")

# @auth_bp.route("/register")
# def register():
#     return render_template("auth/register.html")

# @auth_bp.route("/")
# def login():
#     return render_template("auth/login.html")