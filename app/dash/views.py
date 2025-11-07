from . import dash_bp
from flask import render_template


# ------------------- TEACHER DASHBAORD ROUTES ------------------
@dash_bp.route("/teacher")
def teacher_home():
    return render_template("dashboard/teacher_templates/teacher_create_assignments.html", role="teacher")


# ------------------- ADMIN DASHBAORD ROUTES ------------------
@dash_bp.route("/admin")
def admin_home():
    return render_template("dashboard/admin_templates/admin_create_assignments.html", role="admin")


# ------------------- STUDENT DASHBAORD ROUTES ------------------
@dash_bp.route("/student")
def student_home():
    return render_template("dashboard/student_templates/student_view_all_assignments.html", role="student")


