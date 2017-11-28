from flask import Flask 
from flaskrouter import flaskrouter
from flask_cors import CORS, cross_origin


import models

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:groupPassword@35.193.209.24:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    models.db.init_app(app)
    app.register_blueprint(flaskrouter)
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
    return app

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

if __name__ == "__main__":
    app = create_app()
    app.run()
