from app.database.database import db

class Rol(db.Model):
    __tablename__ = "roles"

    idRol = db.Column(
        db.Integer,
        primary_key=True
    )
    
    nombre = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    # Relación uno a muchos con usuarios
    usuarios = db.relationship(
        "Usuario",
        back_populates="rol",
        lazy=True
    )
