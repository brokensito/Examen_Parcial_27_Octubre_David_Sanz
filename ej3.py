### Parte 1 del ejercicio 3


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


### Comprobacion


carlos = Alumno("Carlos",9)
alberto = Alumno("Alberto",4)
rodrigo = Alumno("Rodrigo",3)
maria = Alumno("Maria", 10)

print(carlos.__str__())
print(alberto.__str__())
print(rodrigo.__str__())
print(maria.__str__())



