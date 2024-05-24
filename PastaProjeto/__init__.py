from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///comunidade.bd"
app.config["SECRET_KEY"]="8784627536ea5cee4cea6640501c9754c8da98ab"
app.config["UPLOAD_FOLDER"] = "static/fotos_post"

database=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="homepage"

from PastaProjeto import routes, forms, models