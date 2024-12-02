from flask import Blueprint, request, jsonify
from datetime import datetime
from .models import Cliente, db

clientes_bp = Blueprint('clientes', __name__)

# Ruta para agregar un nuevo cliente (POST)
@clientes_bp.route('/agregar', methods=['POST'])
def agregar_cliente():
    data = request.get_json()

    # Validar que los campos requeridos estén presentes
    campos_requeridos = ['id', 'nombre_cliente', 'apellidos_cliente', 'tipo_documento', 'genero']
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({"error": f"El campo '{campo}' es requerido"}), 400

    # Crear un nuevo cliente
    nuevo_cliente = Cliente(
        id=data['id'],
        nombre_cliente=data['nombre_cliente'],
        apellidos_cliente=data['apellidos_cliente'],
        tipo_documento=data['tipo_documento'],
        genero=data['genero'],
        fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date() if 'fecha_nacimiento' in data else None,
        telefono=data.get('telefono'),
        correo=data.get('correo'),
        direccion=data.get('direccion'),
        compras=data.get('compras', 0),
        ultima_compra=datetime.strptime(data['ultima_compra'], '%Y-%m-%d').date() if 'ultima_compra' in data else None,
    )

    # Guardar el cliente en la base de datos
    db.session.add(nuevo_cliente)
    db.session.commit()

    return jsonify({"mensaje": "Cliente agregado exitosamente"}), 201


# Ruta para listar todos los clientes (GET)
@clientes_bp.route('/', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    resultado = [
        {
            "id": cliente.id,
            "nombre_cliente": cliente.nombre_cliente,
            "apellidos_cliente": cliente.apellidos_cliente,
            "tipo_documento": cliente.tipo_documento,
            "genero": cliente.genero,
            "fecha_nacimiento": cliente.fecha_nacimiento.isoformat() if cliente.fecha_nacimiento else None,
            "telefono": cliente.telefono,
            "correo": cliente.correo,
            "direccion": cliente.direccion,
            "compras": cliente.compras,
            "ultima_compra": cliente.ultima_compra.isoformat() if cliente.ultima_compra else None,
        }
        for cliente in clientes
    ]
    return jsonify(resultado)


# Ruta para actualizar un cliente existente (PUT)
@clientes_bp.route('/actualizar/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404

    data = request.get_json()

    # Actualizar los campos del cliente
    cliente.nombre_cliente = data.get('nombre_cliente', cliente.nombre_cliente)
    cliente.apellidos_cliente = data.get('apellidos_cliente', cliente.apellidos_cliente)
    cliente.tipo_documento = data.get('tipo_documento', cliente.tipo_documento)
    cliente.genero = data.get('genero', cliente.genero)
    cliente.fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date() if 'fecha_nacimiento' in data else cliente.fecha_nacimiento
    cliente.telefono = data.get('telefono', cliente.telefono)
    cliente.correo = data.get('correo', cliente.correo)
    cliente.direccion = data.get('direccion', cliente.direccion)
    cliente.compras = data.get('compras', cliente.compras)
    cliente.ultima_compra = datetime.strptime(data['ultima_compra'], '%Y-%m-%d').date() if 'ultima_compra' in data else cliente.ultima_compra

    # Guardar cambios en la base de datos
    db.session.commit()

    return jsonify({"mensaje": "Cliente actualizado exitosamente"})


# Ruta para eliminar un cliente (DELETE)
@clientes_bp.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404

    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"mensaje": "Cliente eliminado exitosamente"})
