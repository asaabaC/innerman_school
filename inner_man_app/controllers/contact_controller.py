from flask import Blueprint
from flask import render_template, request, redirect, url_for
from models import db, Contact
from controllers import contact_bp
from extensions import Bcrypt


bcrypt = Bcrypt()

# Blueprint for authentication routes
contact = Blueprint('contact', __name__, url_prefix='/api/v1/contact')

@contact_bp.route('/contact')
def show_contact_form():
    return render_template('contact.html')

@contact_bp.route('/contact', methods=['POST'])
def submit_contact_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    new_contact = Contact(name=name, email=email, message=message)
    db.session.add(new_contact)
    db.session.commit()
    return redirect(url_for('contact_bp.show_contact_form'))
