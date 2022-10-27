lista = [18, 50, 210, 80, 145, 333, 70, 30]

### Estas funciones estan sacadas del libro de algoritmos
def mergesort(lista):

    """Metodo de ordenamiento"""
    if len(lista)<=1:
        return lista
    else: 
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if (izquierda[medio-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda, derecha)
        return resultado

def merge(izquierda, derecha):
    """Funcion para mezclar listas"""
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if (izquierda[0] < derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if (len(izquierda) > 0):
        lista_mezclada += izquierda
    if (len(derecha) > 0):
        lista_mezclada += derecha
    return lista_mezclada

    
####################

def ejercicio1(lista):
    for i, c in enumerate(lista):

        lista_n = []
        if lista[i]%10 == 0 and lista[i]<200:
            lista_n.append(c)

        if i>300:
            break

    return lista_n


n_lista = mergesort(lista)

"""

>>> n_lista = mergesort(lista)
>>> print(n_lista)
[18, 30, 50, 70, 80, 145, 210, 333]

"""
def esta_en_lista(n_lista):
    if 145 in n_lista:
        print(n_lista.index(145))
    else:
        print("-1")

lista_nueva = esta_en_lista(n_lista)

"""
>>> lista_nueva = esta_en_lista(n_lista)
>>> print(lista_nueva)
5

"""

import doctest

if __name__ == "__main__":
    doctest.testmod()








    