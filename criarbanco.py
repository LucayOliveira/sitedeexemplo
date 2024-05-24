from PastaProjeto import app, database
from PastaProjeto.models import Usuario, Foto

with app.app_context():
    database.create_all()
