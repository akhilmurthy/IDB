import os
from flask import Flask, render_template, request 
from flaskrouter import flaskrouter
from models import db

def create_app():
	app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:groupPassword@35.193.209.24/postgres'
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
        db.init_app(app)
        app.register_bluprint(flaskrouter)
	return app
