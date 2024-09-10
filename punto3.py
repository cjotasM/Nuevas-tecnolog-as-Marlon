# Función para determinar si un número es par o impar
def es_par(num):
    return num % 2 == 0

# Función para procesar los 400 números
def procesar_numeros():
    pares = 0
    impares = 0
    listado = []

    # Pedir 400 números al usuario
    for i in range(1, 401):
        numero = int(input(f"Ingrese el número {i}: "))
        if es_par(numero):
            pares += 1
            listado.append((numero, "Par"))
        else:
            impares += 1
            listado.append((numero, "Impar"))

    return listado, pares, impares

# Función para imprimir el listado de números con su clasificación
def imprimir_resultado(listado, pares, impares):
    print("\nListado de Números (Par/Impar):")
    print(f"{'Número':<10} {'Clasificación':<10}")
    print("=" * 20)
    for numero, clasificacion in listado:
        print(f"{numero:<10} {clasificacion:<10}")
    
    print("\nResumen:")
    print(f"Total de números pares: {pares}")
    print(f"Total de números impares: {impares}")

# Ejecutar el programa
listado_numeros, total_pares, total_impares = procesar_numeros()
imprimir_resultado(listado_numeros, total_pares, total_impares)
