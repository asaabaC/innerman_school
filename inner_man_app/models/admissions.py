from flask import request, jsonify
from . import admissions_bp
from models import db, Admission

class Admission(db.Model):
    __tablename__ = "admission"
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    parent_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text, nullable=False)
    applied_grade = db.Column(db.String(10), nullable=False)

@admissions_bp.route('/admissions', methods=['GET', 'POST'])
def handle_admissions():
    if request.method == 'POST':
        data = request.json
        new_admission = Admission(
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
            parent_contact=data['parent_contact']
        )
        db.session.add(new_admission)
        db.session.commit()
        return jsonify({"message": "Admission application submitted"}), 201
    else:
        admissions = Admission.query.all()
        return jsonify([admission.as_dict() for admission in admissions])

@admissions_bp.route('/admissions/<int:id>', methods=['GET'])
def get_admission(id):
    admission = Admission.query.get_or_404(id)
    return jsonify(admission.as_dict())
