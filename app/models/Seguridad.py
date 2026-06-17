from app.database.database import db
from datetime import datetime

class Rol(db.Model):
    __tablename__ = 'roles'
    idRol = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    usuarios = db.relationship('Usuario', backref='rol', lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True)
    idRol = db.Column(db.Integer, db.ForeignKey('roles.idRol'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), nullable=False, unique=True)
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(100), nullable=False, unique=True)
    Contrasena = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
