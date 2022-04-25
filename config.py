
from click import echo
import flask
from model import db
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os



app = flask.Flask(__name__)
Images_Folder = os.path.join('static', 'images')

app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/catlog_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'R8MZNUpaQOlZ85Od838daeuT5VMfj1Qf'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['IMAGES_FOLDER'] = Images_Folder


url = 'postgresql://postgres:postgres@localhost:5432/catlog_db'


engine = create_engine(url, echo = True)

if not database_exists(engine.url):
     create_database(engine.url)
else:
     engine.connect()   



db.init_app(app)

migrate = Migrate(app, db)


with app.app_context():   
     db.create_all() 
        


