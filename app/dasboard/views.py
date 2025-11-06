from flask import Blueprint,render_template


dash_bp = Blueprint("dash",__name__,template_folder="templates",static_folder="static")



# ------------------- ADMIN DASHBAORD ROUTES ------------------
@dash_bp.route("/dashbaord")
def dashbaord():
    return render_template("dasboard/admin_templates/admin_create_assignments.html")


