from app.database.database import db
from sqlalchemy.sql import func
import enum

class EstadoReserva(enum.Enum):
    PENDIENTE = "PENDIENTE"
    ENTREGADO = "ENTREGADO"
    DEVUELTO = "DEVUELTO"
    CANCELADO = "CANCELADO"

class Comprobante(db.Model):
    __tablename__ = 'comprobante'

    idComprobante = db.Column(
        db.Integer,
        primary_key=True
    )
    
    idReserva = db.Column(
        db.Integer,
        db.ForeignKey('reserva.idReserva'),
        nullable=False
    )
    
    numero_comprobante = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )
    
    tipo_comprobante = db.Column(
        db.String(30),
        nullable=False
    )
    
    monto_total = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )
    
    estado = db.Column(
        db.String(30),
        nullable=False
    )
    
    descripcion = db.Column(
        db.Text,
        nullable=True
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

    reserva = db.relationship(
        'Reserva',
        back_populates='comprobantes'
    )

class Reserva(db.Model):
    __tablename__ = 'reserva'

    idReserva = db.Column(
        db.Integer,
        primary_key=True
    )
    
    id_cliente = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.idUsuario'),
        nullable=False
    )
    
    id_administrador = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.idUsuario'),
        nullable=False
    )
    
    fecha_reserva = db.Column(
        db.Date,
        nullable=False,
        server_default=db.text('(CURRENT_DATE)')
    )
    
    fecha_evento = db.Column(
        db.Date,
        nullable=False
    )
    
    fecha_inicio = db.Column(
        db.Date,
        nullable=False
    )
    
    fecha_fin = db.Column(
        db.Date,
        nullable=False
    )
    
    fecha_devolucion = db.Column(
        db.Date,
        nullable=True
    )
    
    estado = db.Column(
        db.Enum(EstadoReserva),
        nullable=False,
        default=EstadoReserva.PENDIENTE
    )
    
    observaciones = db.Column(
        db.Text,
        nullable=True
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
    
    detalles = db.relationship(
        'DetalleReserva',
        back_populates='reserva',
        cascade="all, delete-orphan"
    )
    
    comprobantes = db.relationship(
        'Comprobante',
        back_populates='reserva',
        cascade="all, delete-orphan"
    )
    
    citas = db.relationship(
        'Cita',
        back_populates='reserva',
        cascade="all, delete-orphan"
    )

class DetalleReserva(db.Model):
    __tablename__ = 'detalle_reserva'

    idDetalle_Reserva = db.Column(
        db.Integer,
        primary_key=True
    )
    
    idReserva = db.Column(
        db.Integer,
        db.ForeignKey('reserva.idReserva'),
        nullable=False
    )
    
    idInventario = db.Column(
        db.Integer,
        db.ForeignKey('inventario.idInventario'),
        nullable=False
    )
    
    cantidad = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )
    
    subtotal = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    reserva = db.relationship(
        'Reserva',
        back_populates='detalles'
    )

class Cita(db.Model):
    __tablename__ = 'cita'

    idCita = db.Column(
        db.Integer,
        primary_key=True
    )
    
    id_administrador = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.idUsuario'),
        nullable=False
    )
    
    id_cliente = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.idUsuario'),
        nullable=False
    )
    
    id_reserva = db.Column(
        db.Integer,
        db.ForeignKey('reserva.idReserva'),
        nullable=True
    )
    
    fecha_cita = db.Column(
        db.DateTime,
        nullable=False
    )
    
    motivo = db.Column(
        db.String(150),
        nullable=True
    )
    
    estado = db.Column(
        db.String(30),
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

    reserva = db.relationship(
        'Reserva',
        back_populates='citas'
    )
