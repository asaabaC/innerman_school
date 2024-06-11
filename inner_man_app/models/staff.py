from flask import request, jsonify
from . import staff_bp
from models import db, Staff


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)

@staff_bp.route('/staff', methods=['GET', 'POST'])
def handle_staff():
    if request.method == 'POST':
        data = request.json
        new_staff = Staff(
            name=data['name'],
            position=data['position'],
            contact=data['contact']
        )
        db.session.add(new_staff)
        db.session.commit()
        return jsonify({"message": "Staff member added"}), 201
    else:
        staff = Staff.query.all()
        return jsonify([member.as_dict() for member in staff])

@staff_bp.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    staff_member = Staff.query.get_or_404(id)
    return jsonify(staff_member.as_dict())
