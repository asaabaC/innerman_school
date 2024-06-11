from flask import request, jsonify
from . import contact_bp
from models import db, ContactMessage

@contact_bp.route('/contact', methods=['POST'])
def handle_contact():
    data = request.json
    new_message = ContactMessage(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Contact message sent"}), 201

@contact_bp.route('/contact', methods=['GET'])
def get_messages():
    messages = ContactMessage.query.all()
    return jsonify([message.as_dict() for message in messages])

