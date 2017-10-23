from flask import Flask 
from flaskrouter import flaskrouter

def create_app():
	app = Flask(__name__)
	app.register_blueprint(flaskrouter)
	return app