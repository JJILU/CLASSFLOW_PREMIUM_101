from app.extensions import db
from app.auth.models import Teacher,Admin,Student,TeacherSchoolRecord,StudentSchoolRecord
from datetime import datetime

# =========== Dashboard End-Points ===================

compulsarysubject_class = db.Table(
    "compulsarysubject_class",
    db.Column(db.Integer,db.ForeignKey('compulsarysubject.id')),
    db.Column(db.Integer,db.ForeignKey('classroom.id')),
)

class CompulsarySubject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    classroom_name = db.Column(db.String(50),nullable=False,unique=True) 



class OptionalSubject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    classroom_name = db.Column(db.String(50),nullable=False,unique=True) 


teacher_school_record_class = db.Table(
    "teacher_school_record_class",
    db.Column(db.Integer,db.ForeignKey('seacherschoolrecord.id')),
    db.Column(db.Integer,db.ForeignKey('classroom.id')),
)


class Classroom(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    classroom_name = db.Column(db.String(50),nullable=False,unique=True) 
    # relationships
    compulsary_subjects = db.relationship("CompulsarySubject",secondary=teacher_school_record_class,backref="classroom",lazy="joined")
    optional_subjects = db.relationship("OptionalSubject",backref="classroom",uselist=True,lazy="joined")
    teacher_school_record = db.relationship("TeacherSchoolRecord",secondary=teacher_school_record_class,backref="classroom",lazy="joined")
    student_school_record = db.relationship("StudentSchoolRecord",backref="classroom",uselist=True,lazy="joined")
    # teachers = db.relationship("Teacher",secondary=teacher_class,backref="classroom",lazy="joined")
    # admin = db.relationship("Admin",backref="classroom",uselist=True,lazy="joined")
    # students = db.relationship("Student",backref="classroom",uselist=True,lazy="joined")


class StudentAttendance(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    is_present = db.Column(db.Boolean,nullable=False,default=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)
    # fk
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    # relationships
    student = db.relationship("Student",backref="student_attendance",uselist=False,lazy="joined")


class StudentGrade(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    exam_name = db.Column(db.String(50),nullable=False,unique=True)
    exam_code = db.Column(db.String(50),nullable=False,unique=True)
    exam_subject_Name = db.Column(db.String(50),nullable=False,unique=True)
    classroom_name = db.Column(db.String(50),nullable=False,unique=True)
    student_score = db.Column(db.Integer,nullable=False) 
    student_grade = db.Column(db.String(5),nullable=False) 
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)
    # fk
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    # relationships
    student = db.relationship("Student",backref="student_grade",uselist=False,lazy="joined")


class ClassAssignments(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    assignment_name = db.Column(db.String(50),nullable=False,unique=True)
    assignment_code = db.Column(db.String(50),nullable=False,unique=True)
    assignment_subject_Name = db.Column(db.String(50),nullable=False,unique=True)
    classroom_name = db.Column(db.String(50),nullable=False,unique=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)
    # fk
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    # relationships
    student = db.relationship("Student",backref="student_attendance",uselist=False,lazy="joined")






# =============== AssignmentsFileUpload ================

# class AssignmentsFileUploads(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    # id = db.Column(db.Integer,primary_key=True)   
    # filename = db.Column(db.String(500),nullable=False) 
    # filepath = db.Column(db.String(500),nullable=False) 

    # 1:1 ->  StudentSchoolRecord & FileUploads
    # student_school_record_id = db.Column(db.Integer,db.ForeignKey('studentschoolrecord.id'))