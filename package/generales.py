from package.especificas import *
from os import system

def menu():
    print("""
    \n
    1. Obtener existencias\n
    2. Mostrar cantidad de kilos de cereales por deposito\n
    3. Mostrar cereal que almaceno menos kilos en cada deposito\n
    4. Mostrar maxima cantidad de kilos almacenados de cada cereal\n
    5. Mostrar deposito con mayor recaudacion\n
    6. Mostrar la cantidad de depositos que almacenaron mas de 50000 kilos de cereales\n
    7. Mostrar el porcentaje de kilos de cada cereal sobre el total de kilos y el cereal con el maximo porcentaje\n
    8. Generar informe con la recaudacion de cada deposito\n
    9. Salir
""")
    
def seleccionar_opcion(matriz_ejemplo:list)->None:
    existencias = generar_matriz(0, 20, 4)
    llenar_matriz_valores_aleatorios(existencias)
    system("cls")
    salir = False
    while salir == False:
        menu()
        opcion = get_int("Ingrese una opcion(1-9): ", "Reingrese la opcion(1-9): ", 1, 9)
        match opcion:
            case 1:
                system("cls")
                mostrar_matriz(existencias)
            case 2:
                system("cls")
                cantidad_kilos_cereales = sumar_filas(matriz_ejemplo)
                mostrar_array(cantidad_kilos_cereales)
            case 3:
                system("cls")
                menores_depositos = encontrar_menores_filas(matriz_ejemplo)
                mostrar_array(menores_depositos)
            case 9:
                system("cls")
                print("Saliendo...")
                salir = True
        system("pause")
        system("cls")