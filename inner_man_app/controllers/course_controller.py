from flask import render_template, request, redirect, url_for
from models import db, Course, Teacher
from controllers import course_bp
from extensions import Bcrypt
from flask import Blueprint



bcrypt = Bcrypt()

# Blueprint for authentication routes
course = Blueprint('course', __name__, url_prefix='/api/v1/course')

@course_bp.route('/courses')
def show_courses():
    courses = Course.query.all()
    return render_template('course.html', courses=courses)

@course_bp.route('/course/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        teacher_id = request.form['teacher_id']
        new_course = Course(name=name, teacher_id=teacher_id)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('course_bp.show_courses'))
    teachers = Teacher.query.all()
    return render_template('add_course.html', teachers=teachers)
