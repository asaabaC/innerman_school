from flask import render_template, request, redirect, url_for
from models import db, Student
from controllers import student_bp
from extensions import Bcrypt
from flask import Blueprint


bcrypt = Bcrypt()

# Blueprint for authentication routes
student = Blueprint('student',url_prefix='/api/v1/student')

@student_bp.route('/students')
def show_students():
    students = Student.query.all()
    return render_template('student.html', students=students)

@student_bp.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        new_student = Student(name=name, age=age, grade=grade)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('student_bp.show_students'))
    return render_template('add_student.html')
