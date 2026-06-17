from app.database.database import db
from app.models.album_cancion import album_cancion

class Cancion(db.Model):
    __tablename__ = "cancion"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    minutos = db.Column(db.Integer, nullable=False)
    segundos = db.Column(db.Integer, nullable=False)
    interprete = db.Column(db.String(150), nullable=False)

    albums = db.relationship("Album", secondary=album_cancion, back_populates="canciones")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
