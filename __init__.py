from flask import Flask 
from flaskrouter import flaskrouter
from flask_cors import CORS, cross_origin

import models as models

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:groupPassword@/postgres?host=/cloudsql/overwatchglam-181020:us-central1:overwatch2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
models.db.init_app(app)
app.register_blueprint(flaskrouter)


