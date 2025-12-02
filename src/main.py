from flask import Flask
from routes.api import api
from flask_migrate import Migrate
from extensions.db import db
from dotenv import load_dotenv
load_dotenv()
from config.db import DBConfig

migrate = Migrate()
app = Flask(__name__)

app.config.from_object(DBConfig)
db.init_app(app)
migrate.init_app(app, db)

from models.shortener import Shortnener

app.register_blueprint(api, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)