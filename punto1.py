def generar_serie(n):
    serie = []
    a, b = 5, 8  # Los dos primeros números de la serie

    for _ in range(n):
        if a != 13:  # Omitir el número 13
            serie.append(a)
        a, b = b, a + b  # Generar el siguiente número en la serie
    
    return serie

# Calcular los primeros 100 números de la serie
result = generar_serie(100)

# Mostrar el resultado
print(result)
