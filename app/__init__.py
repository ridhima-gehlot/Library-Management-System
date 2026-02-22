from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


#Create global database
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']='ridhima'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ridhima@localhost/library_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.library import library_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(library_bp)

    return app