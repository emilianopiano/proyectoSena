from extensions import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    apellido_usuario = db.Column(db.String(50), nullable=False)
    tipo_documento = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(20), nullable=True)
    fecha_ultimo_login = db.Column(db.DateTime, nullable=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    perfil = db.Column(db.String(20), nullable=False)
    foto = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Usuario {self.username}>'
