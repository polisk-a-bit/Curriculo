from FakePinterest import app, database
from FakePinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()

# Cria o banco de dados
