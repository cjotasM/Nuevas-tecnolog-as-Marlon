import random

# Parámetros globales
NUM_EMPLEADOS = 1897
SALARIO_BASE = 1300000  # Salario base fijo en pesos
PORCENTAJE_COMISION = 0.05  # 5% de comisiones sobre ventas
PORCENTAJE_SEGURIDAD_SOCIAL = 0.08  # 8% deducción para seguridad social

# Función para calcular el salario de cada empleado
def calcular_salario(ventas):
    comision = ventas * PORCENTAJE_COMISION
    salario_bruto = SALARIO_BASE + comision
    deduccion_seguridad_social = salario_bruto * PORCENTAJE_SEGURIDAD_SOCIAL
    salario_neto = salario_bruto - deduccion_seguridad_social
    return salario_bruto, deduccion_seguridad_social, salario_neto

# Generar el listado de empleados y calcular salarios
def generar_listado_empleados(num_empleados):
    listado = []
    for empleado_id in range(1, num_empleados + 1):
        ventas = random.uniform(1000, 10000)  # Ventas aleatorias entre 1000 y 1000000 pesos
        salario_bruto, deduccion_ss, salario_neto = calcular_salario(ventas)
        listado.append({
            "Empleado ID": empleado_id,
            "Ventas": round(ventas, 2),
            "Salario Bruto": round(salario_bruto, 2),
            "Deducción Seguridad Social": round(deduccion_ss, 2),
            "Salario Neto": round(salario_neto, 2)
        })
    return listado

# Imprimir el listado de empleados
def imprimir_listado_empleados(listado):
    print(f"{'Empleado ID':<12} {'Ventas':<12} {'Salario Bruto':<15} {'Deducción SS':<15} {'Salario Neto':<15}")
    print("=" * 69)
    for empleado in listado:
        print(f"{empleado['Empleado ID']:<12} ${empleado['Ventas']:<11} ${empleado['Salario Bruto']:<14} ${empleado['Deducción Seguridad Social']:<14} ${empleado['Salario Neto']:<14}")

# Generar e imprimir el listado de 1897 empleados
listado_empleados = generar_listado_empleados(NUM_EMPLEADOS)
imprimir_listado_empleados(listado_empleados)
