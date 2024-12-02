# categorias/models.py

from extensions import db
from datetime import datetime

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nombre_categoria}>'
