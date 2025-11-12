from flask import Flask, render_template, request, redirect, url_for
from db_config import db
from mascota import Mascota

class Programa:
    def __init__(self):
        self.app = Flask(__name__)
    
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///estudiantes.sqlite3"
        db.init_app(self.app)
        self.app.add_url_rule('/', view_func=self.mostrartodo)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])

        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)

    def mostrartodo(self):
        return render_template('mostrartodo.html', mascotas=Mascota.query.all())

    def agregar(self):
        if request.method == "POST":
            nombre = request.form['nombre']
            raza = request.form['raza']
            dueño = request.form['dueño']
            edad = request.form['edad']

            mimascota = Mascota(nombre=nombre, raza=raza, edad=edad)
            db.session.add(mimascota)
            db.session.commit()

            return redirect(url_for('mostrartodo'))
       
        return render_template('nuevamascota.html')

miprograma = Programa()
