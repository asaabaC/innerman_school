from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt # for hashing our passwords
from flask_jwt_extended import JWTManager #for creating tokens


db = SQLAlchemy() #handles the ORM related activities
migrate = Migrate()
bcrypt = Bcrypt() # type: ignore
jwt = JWTManager()