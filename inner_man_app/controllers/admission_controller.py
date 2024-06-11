from flask import Blueprint
from flask import  render_template, request, redirect, url_for # type: ignore
from models import db, Admission
from controllers import admission_bp
from extensions import Bcrypt

bcrypt = Bcrypt()

# Blueprint for authentication routes
admission = Blueprint('admission', __name__, url_prefix='/api/v1/admission')


@admission_bp.route('/admissions')
def show_admission_form():
    return render_template('admission.html')

@admission_bp.route('/admissions', methods=['POST'])
def submit_admission_form():
    student_name = request.form['student_name']
    parent_name = request.form['parent_name']
    contact_number = request.form['contact_number']
    address = request.form['address']
    applied_grade = request.form['applied_grade']
    new_admission = Admission(student_name=student_name, parent_name=parent_name, contact_number=contact_number, address=address, applied_grade=applied_grade)
    db.session.add(new_admission)
    db.session.commit()
    return redirect(url_for('admission_bp.show_admission_form'))
