def get_int(mensaje:str, mensaje_error:str, minimo:int = float("-inf"), maximo:int = float("+inf")):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))
    
    return numero