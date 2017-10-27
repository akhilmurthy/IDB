from flask import Flask 
from flaskrouter import flaskrouter

import models

def create_app():
	app = Flask(__name__)
        SQLALCHEMY_DATABASE_URI = \
        '{engine}://{username}:{password}@{hostname}/{database}'.format(
            engine='postgres',
            username='postgres',
            password='groupPassword',
            hostname='35.193.209.24:5432',
database='postgres')
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        models.db.init_app(app)
        app.register_blueprint(flaskrouter)
	return app

if __name__ == "__main__":
    app = create_app()
    app.run()
