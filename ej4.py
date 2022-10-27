from algoritmos.hash import crear_tabla, funcion_hash, cantidad_elementos, agregar, buscar, quitar



def convertir8 (valor: str) -> str:
    if not valor.isascii():
        raise ValueError("No se pueden introducir ASCII")
    return "".join(f"{ord(i):08b}" for i in valor)

