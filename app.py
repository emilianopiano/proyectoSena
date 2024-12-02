# app.py

from flask import Flask
from extensions import db
from categorias import categorias_bp  # Importar el blueprint de categorías
from clientes.routes import clientes_bp  # Importar el blueprint de clientes

# Configuración de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'  # Ruta de la base de datos SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)

# Registrar los Blueprints
app.register_blueprint(categorias_bp, url_prefix='/categorias')  # Rutas de categorías
app.register_blueprint(clientes_bp, url_prefix='/clientes')  # Rutas de clientes

if __name__ == '__main__':
    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)

