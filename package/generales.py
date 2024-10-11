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
    
def seleccionar_opcion()->None:
    existencias = generar_matriz(0, 20, 4)
    llenar_matriz_valores_aleatorios(existencias)
    cereales = ["maiz", "trigo", "cebada", "centeno"]
    valor_cereales = [40, 50, 45, 55]
    system("cls")
    continuar = True
    while continuar:
        menu()
        opcion = get_int("Ingrese una opcion(1-9): ", "Reingrese la opcion(1-9): ", 1, 9)
        match opcion:
            case 1:
                system("cls")
                mostrar_matriz(existencias)
            case 2:
                system("cls")
                cantidad_kilos_cereales_por_deposito = sumar_filas(existencias)
                mostrar_array(cantidad_kilos_cereales_por_deposito)
            case 3:
                system("cls")
                menores_depositos = encontrar_menores_filas(existencias)
                mostrar_array(menores_depositos)
            case 4:
                system("cls")
                maximo_kilos_por_cereal = buscar_maximo_columnas(existencias)
                matriz_con_referencia = generar_matriz_lista_referencia(maximo_kilos_por_cereal, cereales)
                mostrar_matriz(matriz_con_referencia)
            case 5:
                system("cls")
                recaudacion = multiplicar_valores_matriz(valor_cereales, existencias)
                maximas_recaudaciones = buscar_maximo_filas(recaudacion)
                deposito_mas_recaudaciones = buscar_posicion_mayor(maximas_recaudaciones) + 1
                print(f"El deposito con mas recaudaciones es el numero {deposito_mas_recaudaciones}")
            case 6:
                system("cls")
                cantidad_kilos_cereales_por_deposito = sumar_filas(existencias)
                cantidad_depositos_mayor_que_50000 = buscar_cantidad_mayor_a_x_en_array(cantidad_kilos_cereales_por_deposito, 50000)
                print(f"Hay {cantidad_depositos_mayor_que_50000} depositos con mas de 50000 kilos de cereales.")
            case 7:
                system("cls")
                total_cereales = sumar_matriz(existencias)
                cantidad_cereales = sumar_columnas(existencias)
                porcentaje_cereales = calcular_porcentaje_array(cantidad_cereales, total_cereales)
                matriz_porcentajes = generar_matriz_lista_referencia(porcentaje_cereales, cereales)
                mostrar_matriz(matriz_porcentajes)
            case 8:
                system("cls")
                recaudacion = multiplicar_valores_matriz(valor_cereales, existencias)
                recaudacion_por_deposito = sumar_filas(recaudacion)
                recaudacion_por_deposito_ordenada = ordenar_vector(recaudacion_por_deposito)
                mostrar_array(recaudacion_por_deposito_ordenada)

            case 9:
                system("cls")
                print("Saliendo...")
                continuar = False
        system("pause")
        system("cls")