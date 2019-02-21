
from flask_sqlalchemy import SQLAlchemy
db= SQLALchemy()

#Define a Course
class Course(db.model):
    __tablename__= "courses"

    # Specify the columns/ fields of the course
    id = db.Column(db.Integer,primary_key=True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    # Specify any relationship fields.
    registered_students= db.relationship("Registered Students", backref="courses", lazy=True)



class RegisteredStudent(db.Model):
    __tablename__ = "registered_students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.String, nullable=False)

    # Notice, this field serves as a foreighKey.
    course_number = db.Column(db.Integer, db.ForeignKey('course_number.id'), nullable=False)

    # specify any utility methods associated with the model.
    def add_student(self,name, grade ):
        new_register_student = RegisteredStudent(name=name, grade=grade)
        db.session.add(new_student)
        db.session.commit()
