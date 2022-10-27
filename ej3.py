class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con exito")

    def __str__(self):
        return "El alumno {} ha sacado un {} en el examen".format(self.nombre,self.nota)

    def calificacion(self):
        if self.nota>=5:
            mensaje = "El alumno ha APROBADO con una nota de: {}".format(self.nota)

        else:
            mensaje= "El alumno ha SUSPENDIDO con una nota de: {}".format(self.nota)

        return mensaje


