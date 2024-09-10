import random

# Función que devuelve el nivel de leucemia según el puntaje
def clasificar_leucemia(puntaje):
    if puntaje < 10:
        return "No tiene Leucemia"
    elif 11 <= puntaje <= 40:
        return "Nivel bajo de Leucemia"
    elif 41 <= puntaje <= 69:
        return "Nivel moderado de Leucemia"
    else:
        return "Nivel grave de Leucemia"

# Lista para almacenar los datos de los pacientes
listado_pacientes = []

# Generar los puntajes y clasificaciones de 803 pacientes
for paciente_id in range(1, 804):
    puntaje = random.randint(0, 100)
    nivel_leucemia = clasificar_leucemia(puntaje)
    
    # Agregar los datos del paciente a la lista
    listado_pacientes.append((paciente_id, puntaje, nivel_leucemia))

# Mostrar el resultado en pantalla
print(f"{'Paciente ID':<12} {'Puntaje':<10} {'Nivel de Leucemia':<25}")
print("=" * 47)
for paciente in listado_pacientes:
    paciente_id, puntaje, nivel_leucemia = paciente
    print(f"{paciente_id:<12} {puntaje:<10} {nivel_leucemia:<25}")
