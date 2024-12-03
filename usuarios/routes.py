from flask import Blueprint, request, jsonify
from extensions import db
from usuarios.models import Usuario

usuario_bp = Blueprint('usuarios', __name__)

# Ruta para agregar un usuario (POST)
@usuario_bp.route('/agregar', methods=['POST'])
def agregar_usuario():
    data = request.get_json()

    nuevo_usuario = Usuario(
        id_usuario=data['id_usuario'],
        nombre_usuario=data['nombre_usuario'],
        apellido_usuario=data['apellido_usuario'],
        tipo_documento=data['tipo_documento'],
        username=data['username'],
        password=data['password'],
        genero=data.get('genero'),
        perfil=data['perfil'],
        foto=data.get('foto'),
        fecha_creacion=data.get('fecha_creacion', None) or None,
        fecha_ultimo_login=data.get('fecha_ultimo_login', None) or None,
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario agregado exitosamente"}), 201

# Ruta para listar usuarios (GET)
@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    resultado = [
        {
            "id_usuario": usuario.id_usuario,
            "nombre_usuario": usuario.nombre_usuario,
            "apellido_usuario": usuario.apellido_usuario,
            "tipo_documento": usuario.tipo_documento,
            "username": usuario.username,
            "genero": usuario.genero,
            "fecha_ultimo_login": usuario.fecha_ultimo_login.isoformat() if usuario.fecha_ultimo_login else None,
            "fecha_creacion": usuario.fecha_creacion.isoformat(),
            "perfil": usuario.perfil,
            "foto": usuario.foto,
        }
        for usuario in usuarios
    ]
    return jsonify(resultado)

# Ruta para eliminar un usuario por ID (DELETE)
@usuario_bp.route('/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario eliminado exitosamente"}), 200
