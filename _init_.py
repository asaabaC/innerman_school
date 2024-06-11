from flask import Flask, jsonify
from config import Config
from extensions import bcrypt, db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['DEBUG'] = True

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import models
    from inner_man_app.models import student
    from inner_man_app.models import staff
    from inner_man_app.models import course
    from inner_man_app.models import contact
    
    
    
    #importing blueprints
    
    app.register_blueprint('staff',url_prefix='/api/v1/staff')
    app.register_blueprint('contact', __name__, url_prefix='/api/v1/contact')
    app.register_blueprint('course', __name__, url_prefix='/api/v1/course')
    app.register_blueprint('student',url_prefix='/api/v1/student')
    app.register_blueprint('admission', __name__, url_prefix='/api/v1/admission')


 


    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to Innerman Primary School"})

    return app

app = create_app()
















# from flask import Flask
# from config import Config
# from extensions import bcrypt, db, migrate, jwt


# app = Flask(__name__)
# app.config.from_object(Config)

# db.init_app(app)

# with app.app_context():
#     db.create_all()
    
    
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
    
#     app.config['DEBUG'] =True
    
#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     bcrypt.init_app(app)
#     jwt.init_app(app)
    
#     #Import models
#     from inner_man_app.models import student
#     from inner_man_app.models import staff
#     from inner_man_app.models import course
#     from inner_man_app.models import contact
    
    

#     # Test route
#     @app.route('/')
#     def home():
#         return "Authors API setup"



# @app.route('/')
# def index():
#     return jsonify({"message": "Welcome to Innerman Primary School "}) # type: ignore

# if __name__ == "__main__":
#     app=create_app()
#     app.run(debug=True)

