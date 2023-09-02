    from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.climate._flaskApp import climate
from project.log._flaskApp import log


# app config
app = Flask(__name__)

app.config.from_object("project.config.Config")

app.register_blueprint(climate, url_prefix='/climate')
app.register_blueprint(log, url_prefix='/log')

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
