#programa para la Gestión de estudiantes

#1ra parte: en estas lineas de codigo establecere el diccionario con los valores de notas y nombres 
#la clave será la cédula o ID, y el valor será otro diccionario con nombre y notas
estudiantes = {}

#2da parte: en esta lienas de codigo puedo registrar estudiantes
def registrar_estudiante():
    print("\n--- Registrar Estudiante ---")
    id_estudiante = input("Ingrese el ID o cédula del estudiante: ")
    
    if id_estudiante in estudiantes:
        print("El estudiante con este ID ya está registrado.")
    else:
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiantes[id_estudiante] = {
            "nombre": nombre,
            "notas": []
        }
        print(f"Estudiante {nombre} registrado con éxito.")

#3ra parte: estas lineas de codigo me sirven para listar estudiantes
def listar_estudiantes():
    print("\n--- Listar Estudiantes ---")
    
    if not estudiantes:
        print(" No hay estudiantes registrados.")
    else:
        for id_estudiante, datos in estudiantes.items():
            print(f"ID: {id_estudiante} | Nombre: {datos['nombre']} | Notas: {datos['notas']}")

#4ta parte: aqui puedo establecer la funcion para buscar a cada estudiante
def buscar_estudiante():
    print("\n--- Buscar Estudiante ---")
    id_estudiante = input("Ingrese el ID o cédula del estudiante a buscar: ")
    
    if id_estudiante in estudiantes:
        datos = estudiantes[id_estudiante]
        print(f"ID: {id_estudiante} | Nombre: {datos['nombre']} | Notas: {datos['notas']}")
    else:
        print("Estudiante no encontrado.")

#5ta parte: Función que me servira para registrar notas
def registrar_notas():
    print("\n--- Registrar Notas ---")
    id_estudiante = input("Ingrese el ID o cédula del estudiante: ")
    
    if id_estudiante in estudiantes:
        try:
            cantidad = int(input("¿Cuántas notas desea registrar? "))
            for i in range(cantidad):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i+1}: "))
                        if 0 <= nota <= 5:  # Suponiendo escala 0 a 5
                            estudiantes[id_estudiante]["notas"].append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 5.")
                    except ValueError:
                        print("Debe ingresar un número válido.")
            print(f"✅ Notas registradas para {estudiantes[id_estudiante]['nombre']}.")
        except ValueError:
            print("Debe ingresar un número entero válido para la cantidad de notas.")
    else:
        print("Estudiante no encontrado.")

#6ta parte: Función que me permititira calcular el promedio
def calcular_promedio():
    print("\n--- Calcular Promedio ---")
    id_estudiante = input("Ingrese el ID o cédula del estudiante: ")
    
    if id_estudiante in estudiantes:
        notas = estudiantes[id_estudiante]["notas"]
        if notas:
            promedio = sum(notas) / len(notas)
            print(f"El promedio de {estudiantes[id_estudiante]['nombre']} es: {promedio:.2f}")
        else:
            print("Este estudiante no tiene notas registradas.")
    else:
        print("Estudiante no encontrado.")

#aqui pongo el menu para interactuar:
def menu():
    while True:
        print("\n--- MENÚ DE GESTIÓN DE ESTUDIANTES ---")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Buscar estudiante")
        print("4. Registrar notas")
        print("5. Calcular promedio")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            registrar_notas()
        elif opcion == "5":
            calcular_promedio()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
menu()
