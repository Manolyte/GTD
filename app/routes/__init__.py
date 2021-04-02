from flask import request, render_template
from app import app, db
from app.models.Tarea import Tarea
from datetime import datetime


@app.route("/")
def index():
    titulo = "Gestión de Agenda"
    return render_template("index.html", titulo=titulo)


@app.route("/Tarea")
def tarea():
    titulo = "Gestión de Tareas"
    return render_template("tarea.html", titulo=titulo)


@app.route("/nuevaTarea", methods=["GET","POST"])
def nuevaTarea():
    titulo = "Nueva Tarea"
    if request.method == "POST":
        tarea = request.form["tarea"]
        duracion = request.form["duracion"]
        estado = "P"
        orden = Tarea.query.filter_by(idactividad=request.form["idactividad"]).count() + 1
        fecFin = request.form["fecFin"]
        fecRegistro = datetime.now()
        fecModificacion = None
        idactividad = request.form["idactividad"]
        idtareapadre = None

        if tarea == "" or idactividad == "":
            return render_template("tarea.html", titulo=titulo, mensaje="Por favor, ingrese los datos obligatorios")

        data = Tarea(tarea, duracion, estado, orden, fecFin, fecRegistro, fecModificacion, idactividad, idtareapadre)
        db.session.add(data)
        db.session.commit()
        return render_template("tarea.html", titulo=titulo, mensaje="Datos Registrados Satisfactoriamente")