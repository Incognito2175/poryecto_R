from app.database.database import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    idUsuario = db.Column(
        db.Integer,
        primary_key=True
    )
    
    idRol = db.Column(
        db.Integer,
        db.ForeignKey("roles.idRol"),
        nullable=False
    )
    
    nombre = db.Column(
        db.String(100),
        nullable=False
    )
    
    documento = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )
    
    telefono = db.Column(
        db.String(20),
        nullable=True
    )
    
    correo = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )
    
    contrasena = db.Column(
        db.String(255),
        nullable=False
    )
    
    avatar = db.Column(
        db.String(255),
        nullable=True,
        default="default.png"
    )
    
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
    
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    # Relaciones bidireccionales
    rol = db.relationship(
        "Rol",
        back_populates="usuarios"
    )
