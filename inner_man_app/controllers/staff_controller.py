from flask import render_template, request, redirect, url_for
from models import db, Teacher
from controllers import teacher_bp
from extensions import Bcrypt
from flask import Blueprint



bcrypt = Bcrypt()

# Blueprint for authentication routes
staff = Blueprint('staff', __name__, url_prefix='/api/v1/staff')

@teacher_bp.route('/teachers')
def show_teachers():
    teachers = Teacher.query.all()
    return render_template('teacher.html', teachers=teachers)

@teacher_bp.route('/teacher/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        new_teacher = Teacher(name=name, subject=subject)
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for('teacher_bp.show_teachers'))
    return render_template('add_teacher.html')
