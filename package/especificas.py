from random import *

def get_int(mensaje:str, mensaje_error:str, minimo:int = float("-inf"), maximo:int = float("+inf")):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))
    
    return numero

def generar_matriz(valor_inicial:any, filas:int, columnas:int)->list:
    matriz = [0] * filas
    for i in range(len(matriz)):
        matriz[i] = [valor_inicial] * columnas
    
    return matriz

def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()

def llenar_matriz_valores_aleatorios(matriz:list)->list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = randint(5000, 20000)