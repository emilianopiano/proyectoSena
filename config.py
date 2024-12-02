class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tienda.db'  # Base de datos SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False          # Desactiva las advertencias de cambios
    SECRET_KEY = 'mi_secreto_super_seguro'
