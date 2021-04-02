from app import db

class Tarea(db.Model):
    __tablename__ = 'tarea'

    idtarea = db.Column(db.Integer, primary_key=True)
    tarea = db.Column(db.String())
    duracion = db.Column(db.Integer)
    estado = db.Column(db.String())
    orden = db.Column(db.Integer)
    fecFin = db.Column(db.String())
    fecRegistro = db.Column(db.String())
    fecModificacion = db.Column(db.String())
    idactividad = db.Column(db.Integer)
    idtareapadre = db.Column(db.Integer)

    def __init__(self, tarea, duracion, estado, orden, fecFin, fecRegistro, fecModificacion, idactividad, idtareapadre):
        self.tarea = tarea
        self.duracion = duracion
        self.estado = estado
        self.orden = orden
        self.fecFin = fecFin
        self.fecRegistro = fecRegistro
        self.fecModificacion = fecModificacion
        self.idactividad = idactividad
        self.idtareapadre = idtareapadre