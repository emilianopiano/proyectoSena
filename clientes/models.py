from extensions import db
from datetime import date

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.Text, nullable=False)
    apellidos_cliente = db.Column(db.Text, nullable=False)
    tipo_documento = db.Column(db.Text, nullable=False)
    genero = db.Column(db.Text, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    telefono = db.Column(db.Text, nullable=True)
    correo = db.Column(db.Text, unique=True, nullable=True)
    direccion = db.Column(db.Text, nullable=True)
    compras = db.Column(db.Integer, default=0, nullable=False)
    ultima_compra = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Cliente {self.nombre_cliente} {self.apellidos_cliente}>"
