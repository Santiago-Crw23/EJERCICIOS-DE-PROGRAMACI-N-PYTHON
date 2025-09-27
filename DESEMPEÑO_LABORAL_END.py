# PARTE 1: Definir colaboradores
# =======================
colaboradores = [
    {"nombre": "Juan", "desempeno": []},
    {"nombre": "María", "desempeno": []},
    {"nombre": "Pedro", "desempeno": []}
]

print("=== Lista de colaboradores definida ===")
for c in colaboradores:
    print(f"Colaborador: {c['nombre']} | Datos iniciales: {c['desempeno']}")

# =======================
# PARTE 2: Registro diario de desempeño
# =======================
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias:
    print(f"\n=== {dia.upper()} ===")
    for c in colaboradores:
        print(f"\nIngrese los datos de desempeño para {c['nombre']}:")
        
        puntualidad = float(input("Puntualidad (0-10): "))
        calidad = float(input("Calidad (0-10): "))
        colaboracion = float(input("Colaboración (0-10): "))
        eficiencia = float(input("Eficiencia (0-10): "))
        
        promedio_dia = (puntualidad + calidad + colaboracion + eficiencia) / 4
        c["desempeno"].append(promedio_dia)
        
        print("Reporte ingresado con éxito ✅")
    
    if dia == "Viernes":
        print("\n>>> Generar reporte semanal <<<")

# =======================
# PARTE 3: Cálculo de promedios semanales
# =======================
for c in colaboradores:
    promedios_diarios = c["desempeno"]
    promedio_semanal = sum(promedios_diarios) / len(promedios_diarios)
    c["promedio_semanal"] = promedio_semanal

# (Para verificar ahora mismo)
print("\n=== Verificación de promedios semanales ===")
for c in colaboradores:
    print(f"{c['nombre']} → Promedio semanal: {c['promedio_semanal']:.2f}")

# PARTE 4: Clasificación del desempeño
# =======================
for c in colaboradores:
    promedio = c["promedio_semanal"]
    
    if promedio >= 8.0:
        c["clasificacion"] = "Rendimiento Sobresaliente"
    elif promedio >= 6.0:
        c["clasificacion"] = "Rendimiento Aceptable"
    else:
        c["clasificacion"] = "Rendimiento Bajo"

# PARTE 5: Reporte final
# =======================
print("\n===== REPORTE SEMANAL =====")
for c in colaboradores:
    print(f"\nColaborador: {c['nombre']}")
    print(f"Promedio semanal: {c['promedio_semanal']:.2f}")
    print(f"Desempeño: {c['clasificacion']}")