class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con exito")

    def calificacion(self):
        if self.nota>=5:
            mensaje = "El alumno ha APROBADO con una nota de: {}".format(self.nota)

        else:
            mensaje= "El alumno ha SUSPENDIDO con una nota de: {}".format(self.nota)

        return mensaje


"""Experimentacion"""

carlos = Alumno("Carlos",9)
alberto = Alumno("Alberto",4)
rodrigo = Alumno("Rodrigo",3)
maria = Alumno("Maria", 10)

print(carlos.calificacion())
print(alberto.calificacion())
print(rodrigo.calificacion())
print(maria.calificacion())





