### Parte 1 del ejercicio 3


class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con exito")

    def __str__(self):
        """
        La funcion str sirve para imprimir las caracteristicas que se establecen previamente

        >>> rodrigo = Alumno("Rodrigo", 10)
        >>> print(rodrigo.__str__())
        
        """
        return "El alumno {} ha sacado un {} en el examen".format(self.nombre,self.nota)

    def calificacion(self):
        if self.nota>=5:
            mensaje = "El alumno ha APROBADO con una nota de: {}".format(self.nota)

        else:
            mensaje= "El alumno ha SUSPENDIDO con una nota de: {}".format(self.nota)

        return mensaje




""""
Testeamos las funciones de str para ver que nos sale
>>> carlos = Alumno("Carlos",9)
>>> alberto = Alumno("Alberto",4)
>>> rodrigo = Alumno("Rodrigo",3)
>>> maria = Alumno("Maria", 10)

>>> print(carlos.__str__())
El alumno Carlos ha sacado un 9 en el examen

>>> print(alberto.__str__())
El alumno Alberto ha sacado un 4 en el examen

>>> print(rodrigo.__str__())
El alumno Rodrigo ha sacado un 3 en el examen

>>> print(maria.__str__())
El alumno Maria ha sacado un 10 en el examen

"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()



