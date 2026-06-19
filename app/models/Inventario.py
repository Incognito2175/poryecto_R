from app.database.database import db
import enum

class EstadoInventario(enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    ALQUILADO = "ALQUILADO"
    MANTENIMIENTO = "MANTENIMIENTO"

class Categoria(db.Model):
    __tablename__ = 'categoria'

    idCategoria = db.Column(
        db.Integer,
        primary_key=True
    )
    
    nombre = db.Column(
        db.String(50),
        nullable=False
    )
    
    prendas = db.relationship(
        'Prenda',
        back_populates='categoria',
        lazy=True
    )

class Prenda(db.Model):
    __tablename__ = 'prenda'

    idPrenda = db.Column(
        db.Integer,
        primary_key=True
    )
    
    idCategoria = db.Column(
        db.Integer,
        db.ForeignKey('categoria.idCategoria'),
        nullable=False
    )
    
    nombre_prenda = db.Column(
        db.String(100),
        nullable=False
    )
    
    descripcion = db.Column(
        db.Text,
        nullable=True
    )
    
    talla = db.Column(
        db.String(10),
        nullable=False
    )
    
    color = db.Column(
        db.String(30),
        nullable=False
    )
    
    precio_alquiler = db.Column(
        db.Numeric(10, 2),
        nullable=False
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

    categoria = db.relationship(
        'Categoria',
        back_populates='prendas'
    )
    
    items_inventario = db.relationship(
        'Inventario',
        back_populates='prenda',
        lazy=True
    )

class Inventario(db.Model):
    __tablename__ = 'inventario'

    idInventario = db.Column(
        db.Integer,
        primary_key=True
    )
    
    idPrenda = db.Column(
        db.Integer,
        db.ForeignKey('prenda.idPrenda'),
        nullable=False
    )
    
    codigo_interno = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )
    
    estado = db.Column(
        db.Enum(EstadoInventario),
        nullable=False,
        default=EstadoInventario.DISPONIBLE
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

    prenda = db.relationship(
        'Prenda',
        back_populates='items_inventario'
    )
