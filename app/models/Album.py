from app.database.database import db
from app.models.medio import Medio
from app.models.album_cancion import album_cancion

class Album(db.Model):
    __tablename__ = "album"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text)
    medio = db.Column(db.Enum(Medio), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)

    usuario = db.relationship("Usuario", back_populates="albums")
    canciones = db.relationship("Cancion", secondary=album_cancion, back_populates="albums")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
