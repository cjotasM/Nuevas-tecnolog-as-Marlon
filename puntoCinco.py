import random

# Función para clasificar el funcionamiento de la cabina según el puntaje
def clasificar_funcionamiento(puntaje):
    if puntaje == 2:
        return "Funcionamiento defectuoso"
    elif puntaje == 3:
        return "Funcionamiento moderado"
    elif puntaje == 4:
        return "Funcionamiento óptimo"
    else:
        return "Puntaje inválido"  # Para asegurarse de que solo se acepten puntajes 2, 3 o 4

# Lista para almacenar los datos de las cabinas
listado_cabinas = []

# Generar los puntajes y clasificaciones para 407 cabinas
for cabina_id in range(1, 408):
    puntaje = random.choice([2, 3, 4])  # Puntaje aleatorio de entre 2, 3 y 4
    funcionamiento = clasificar_funcionamiento(puntaje)
    
    # Agregar los datos de la cabina a la lista
    listado_cabinas.append((cabina_id, puntaje, funcionamiento))

# Mostrar el resultado en pantalla
print(f"{'Cabina ID':<10} {'Puntaje':<7} {'Funcionamiento':<25}")
print("=" * 42)
for cabina in listado_cabinas:
    cabina_id, puntaje, funcionamiento = cabina
    print(f"{cabina_id:<10} {puntaje:<7} {funcionamiento:<25}")
