from db import db 

class Mascota(db.Model): #usar mayusculas para las clases
    _tablename_="mascota"

    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    raza=db.Column(db.String(70))
    edad=db.Column(db.String(15))

    def __init__(self,nombre, raza, dueño, edad):
        self.nombre=nombre
        self.raza= raza
        self.dueño=dueño
        self.edad= edad
