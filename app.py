# app.py

from flask import Flask
from extensions import db
from categorias import categorias_bp
from clientes.routes import clientes_bp
from usuarios.routes import usuario_bp  # Importar el blueprint de usuarios

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)

# Registrar los Blueprints
app.register_blueprint(categorias_bp, url_prefix='/categorias')
app.register_blueprint(clientes_bp, url_prefix='/clientes')
app.register_blueprint(usuario_bp, url_prefix='/usuarios')  # Registrar rutas de usuarios

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
