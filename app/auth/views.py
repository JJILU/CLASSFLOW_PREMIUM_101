from . import auth_bp
from flask import (render_template,redirect,
    render_template,
    url_for,flash,
    request,
    jsonify)
from app.auth.models import (
    TeacherSchoolRecord,
    StudentSchoolRecord,
    Teacher,
    Student,
    Admin)
from app.extensions import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('auth/index.html')
    else:
        data = request.get_json()
        print("registered: ",data)

        # check if data was not submitted
        if not data:
            return jsonify({"error": "No data submitted!"}),400
        

        
        missing_fields = []
        
        # check if correct role is selected
        valid_roles = {"teacher","admin","student"}
        if data.get("role") not in valid_roles:
            return jsonify({"error":"Invalid role selected"}),400

        # check if all id and password are submitted
        if  data.get("role") == "Teacher":
            if not data.get("school_id"):     
                missing_fields.append("teacher id missing")    
            if not data.get("password"):
                missing_fields.append("teacher password missing")    



        if  data.get("role") == "Admin":
            if not data.get("school_id"):     
                missing_fields.append("admin id missing")    
            if not data.get("password"):
                missing_fields.append("admin password missing")     

        if  data.get("role") == "Student":
            if not data.get("school_id"):     
                missing_fields.append("student id missing")    
            if not data.get("password"):
                missing_fields.append("student password missing")            
                       
        # if true contains list of missing fields error messages 
        if missing_fields:
            return jsonify({"error":missing_fields}),400    
        

        # extract data from request
        school_id = data.get("school_id")
        password = data.get("password")
        role = data.get("role")


        # check if ID is in school records
        valid_user=None
        if role == "Teacher":
           valid_user =  TeacherSchoolRecord.get_teacher_by_card_id(school_id)
           if not valid_user:
            return jsonify({"error":f"No teacher with school id {school_id} found in school records"}),400
        elif role == "Admin":
           valid_user =  StudentSchoolRecord.get_student_by_card_id(school_id)
           if not valid_user:
            return jsonify({"error":f"No admin with school id {school_id} found in school records"}),400
        else:
           valid_user =  StudentSchoolRecord.get_student_by_card_id(school_id)
           if not valid_user:
            return jsonify({"error":f"No student with school id {school_id} found in school records"}),400

        


        # check if data exists in Teacher,Admin,Student
        if  role == "Teacher" and Teacher.query.filter_by(teacher_card_id=school_id).first():
            return jsonify({"error": "Teacher account with this id already exists"}),400
        if  role == "Admin" and Admin.query.filter_by(admin_card_id=school_id).first():
            return jsonify({"error": "Admin account with this id already exists"}),400
        if  role == "Student" and Student.query.filter_by(student_card_id=school_id).first():
            return jsonify({"error": "Student account with this id already exists"}),400
        

        


        # if record doesn't already exist create a record
        r = None
        if role == "Teacher":
            r = Teacher(teacher_card_id=school_id,password=password,role=role)
        elif role == "Admin":
            r = Admin(admin_card_id=school_id,password=password,role=role) 
        else:
            r = Student(student_card_id=school_id,password=password,role=role)    

        try:    
            db.session.add(r)    
            db.session.commit()  
            return jsonify({"success":"registered successfully,"}),201  
        except Exception as e:
            db.session.rollback()
            print(f"Failed to register user: {str(e)}")
            return jsonify({"success":"failed to register user"}),500
        finally:
            db.session.close()


        
        
        
    


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/index.html")
    else: 
        data = request.get_json()
        print("logged in: ",data)

        # check if data submitted is valid
        return jsonify({"message":"logged in"}),200

