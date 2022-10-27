from algoritmos.hash import crear_tabla, funcion_hash, agregar



def convertir8 (valor: str) -> str:
    if not valor.isascii():
        raise ValueError("No se pueden introducir ASCII")
    return "".join(f"{ord(i):08b}" for i in valor)

def binario_decimal(num):
    return int(num,2)


t_1 = crear_tabla(255)
t_2 = crear_tabla(255)

for i in range(32, 126):
    agregar(t_1, chr(i), convert = False)

for j in range(32, 126):
    agregar(t_2, chr(j), convert=True )


valor = "H"

codificar = t_2[funcion_hash(ord(valor), len(t_2))]

decodificacion = binario_decimal(codificar)

caracter = t_1[decodificacion%len(t_1)]

