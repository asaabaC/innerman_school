from flask_sqlalchemy import SQLAlchemy
from app import app


db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    

def __init__(self, id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        
        # self.isbn = isbn
        # self.genre = genre
        # self.description = description
        # self.image = image
        # self.user_id = user_id
        # self.company_id = company_id

def get_full_name(self):
        return self.title