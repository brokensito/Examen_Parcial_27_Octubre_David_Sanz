
matriz = [[1,5,7,2,5], [2,0,9,2,6], [7,8,9,2,5], [1,5,8,2,4],[0,5,7,2,6]]



def cogerfactor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]         

def determinante(matriz):

    if len(matriz)==2:
        valor = matriz[0][0] * matriz [1][1] - matriz [1][0]

    suma = 0

    for columna_actual in range(len(matriz)):

        signo = (-1) ** (columna_actual)
        sub_det = determinante(cogerfactor(matriz, 0, columna_actual))
        suma += (signo * matriz[0][columna_actual] * sub_det)

    return suma

print("El determinante de la matriz es:", determinante(matriz))

    