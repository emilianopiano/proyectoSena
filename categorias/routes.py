from flask import Blueprint, request, jsonify
from datetime import datetime
from .models import Categoria, db

categorias_bp = Blueprint('categorias', __name__)

# Ruta para agregar una nueva categoría (POST)
@categorias_bp.route('/agregar', methods=['POST'])
def agregar_categoria():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud

    # Validación de la fecha
    fecha_registro = data.get('fecha_registro', '')  # Obtener la fecha, si no existe, usar cadena vacía

    if fecha_registro:
        try:
            # Intentar convertir la fecha proporcionada a un objeto datetime
            fecha_registro = datetime.fromisoformat(fecha_registro)
        except ValueError:
            return jsonify({"mensaje": "Formato de fecha inválido. Use 'YYYY-MM-DDTHH:MM:SS'."}), 400
    else:
        # Si no se proporciona una fecha, usamos la fecha y hora actual
        fecha_registro = datetime.utcnow()

    # Crear una nueva categoría
    nueva_categoria = Categoria(
        nombre_categoria=data['nombre_categoria'],
        descripcion=data.get('descripcion', ''),  # Usar valor vacío si no se proporciona
        fecha_registro=fecha_registro  # Asignar la fecha convertida
    )

    # Agregar la nueva categoría a la base de datos
    db.session.add(nueva_categoria)
    db.session.commit()  # Guardar los cambios

    return jsonify({"mensaje": "Categoría agregada exitosamente"}), 201

# Ruta para listar todas las categorías (GET)
@categorias_bp.route('/', methods=['GET'])
def listar_categorias():
    categorias = Categoria.query.all()  # Obtener todas las categorías
    resultado = [
        {
            "id_categoria": categoria.id_categoria,
            "nombre_categoria": categoria.nombre_categoria,
            "descripcion": categoria.descripcion,
            "fecha_registro": categoria.fecha_registro.isoformat(),  # Convertir la fecha a formato ISO
        }
        for categoria in categorias
    ]
    return jsonify(resultado)  # Devolver las categorías como JSON
