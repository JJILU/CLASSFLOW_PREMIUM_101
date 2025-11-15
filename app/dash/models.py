from app.extensions import db






# =============== AssignmentsFileUpload ================

# class AssignmentsFileUploads(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    # id = db.Column(db.Integer,primary_key=True)   
    # filename = db.Column(db.String(500),nullable=False) 
    # filepath = db.Column(db.String(500),nullable=False) 

    # 1:1 ->  StudentSchoolRecord & FileUploads
    # student_school_record_id = db.Column(db.Integer,db.ForeignKey('studentschoolrecord.id'))