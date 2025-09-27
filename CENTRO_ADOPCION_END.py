mascota1 = {
    'id': 1,
    'nombre': 'Fido',
    'especie': 'perro',
    'raza': 'mestizo',
    'edad_meses': "18 meses",
    'tamano': 'mediano',
    'sexo': 'macho',
    'temperamento': ['juguetón', 'leal', 'energético'],
    'con_ninos': True,
    'nivel_energia': 5,
    'vacunas': True,
    'esterilizado': True,
    'salud': 'Excelente, sin problemas conocidos.',
    'peso_kg': 15.5,
    'descripcion': 'Fido es un perro muy activo que disfruta de largas caminatas y juegos en el parque. Es muy amigable con otros perros y le encanta la compañía.',
}

mascota2 = {
    'id': 2,
    'nombre': 'Luna',
    'especie': 'gato',
    'raza': 'siames',
    'edad_meses': "36 meses",
    'tamano': 'pequeño',
    'sexo': 'hembra',
    'temperamento': ['tranquila', 'cariñosa', 'reservada'],
    'con_ninos': False,
    'nivel_energia': 2,
    'vacunas': True,
    'esterilizado': True,
    'salud': 'Requiere un control veterinario anual, sin enfermedades crónicas.',
    'peso_kg': 4.2,
    'descripcion': 'Luna es una gata elegante que prefiere los ambientes silenciosos. Disfruta de siestas largas en la ventana y de recibir mimos suaves.',
}

mascota3 = {
    'id': 3,
    'nombre': 'Max',
    'especie': 'perro',
    'raza': 'labrador retriever',
    'edad_meses': "48 meses",
    'tamano': 'grande',
    'sexo': 'macho',
    'temperamento': ['obediente', 'sociable', 'paciente'],
    'con_ninos': True,
    'nivel_energia': 4,
    'vacunas': True,
    'esterilizado': False,
    'salud': 'Saludable, sin historial de enfermedades.',
    'peso_kg': 32.0,
    'descripcion': 'Max es un perro familiar por excelencia, ideal para una casa con jardín. Le encanta nadar y es muy bueno con los niños.',
}

mascota4 = {
    'id': 4,
    'nombre': 'Milo',
    'especie': 'gato',
    'raza': 'persa',
    'edad_meses': "12 meses",
    'tamano': 'pequeño',
    'sexo': 'macho',
    'temperamento': ['curioso', 'juguetón'],
    'con_ninos': True,
    'nivel_energia': 3,
    'vacunas': True,
    'esterilizado': True,
    'salud': 'Requiere cepillado diario por su pelo largo.',
    'peso_kg': 3.5,
    'descripcion': 'Milo es un joven gato lleno de curiosidad. Le gusta explorar cada rincón de la casa y jugar con plumas y pelotas.',
}

mascota5 = {
    'id': 5,
    'nombre': 'Bella',
    'especie': 'perro',
    'raza': 'chihuahua',
    'edad_meses': "24 meses",
    'tamano': 'pequeño',
    'sexo': 'hembra',
    'temperamento': ['nerviosa', 'protectora'],
    'con_ninos': False,
    'nivel_energia': 3,
    'vacunas': True,
    'esterilizado': True,
    'salud': 'En buena salud, necesita atención dental periódica.',
    'peso_kg': 2.8,
    'descripcion': 'Bella es una perrita leal y muy apegada a su dueño. Prefiere los ambientes tranquilos y es ideal para vivir en un apartamento.',
}

mascota6 = {
    'id': 6,
    'nombre': 'Simba',
    'especie': 'gato',
    'raza': 'mestizo',
    'edad_meses': "8 meses",
    'tamano': 'pequeño',
    'sexo': 'macho',
    'temperamento': ['muy sociable', 'amigable'],
    'con_ninos': True,
    'nivel_energia': 5,
    'vacunas': True,
    'esterilizado': False,
    'salud': 'Saludable y en crecimiento.',
    'peso_kg': 1.9,
    'descripcion': 'Simba es un gatito que fue rescatado. Es muy sociable y se adapta fácilmente a nuevas personas y entornos. Le encanta jugar con todo lo que se mueve.',
}

lista_mascotas = [mascota1, mascota2, mascota3, mascota4, mascota5, mascota6]

preferencias_usuario = {
    'especie': '',
    'sexo': '',
    'con_ninos': True
}

#2. Preferencias de usuario: que permitira al usuario filtrar masoctas con base en sus proferencias. 
def sugerir_mascotas(lista_mascotas, preferencias_usuario):
    sugerencias = []
    for mascota in lista_mascotas:
        if mascota['especie'] != preferencias_usuario['especie']:
            continue  

        puntaje = 0
        if mascota['tamano'] == preferencias_usuario['tamano']:
            puntaje += 1
        if mascota['sexo'] == preferencias_usuario['sexo']:
            puntaje += 1
        if mascota['con_ninos'] == preferencias_usuario['con_ninos']:
            puntaje += 1
        sugerencias.append((mascota, puntaje))

    sugerencias.sort(key=lambda x: x[1], reverse=True)
    return sugerencias

#3. Funciones para el filtrado de mascotas: que permitira al usuario filtrar las mascotas con base en los atributos de las mismas
def filtrar_mascotas(lista_mascotas, especie=None, sexo=None):
    resultado = []
    for mascota in lista_mascotas:
        if especie and mascota['especie'] != especie:
            continue
        if sexo and mascota['sexo'] != sexo:
            continue
        resultado.append(mascota)
    return resultado


#4. Programa principal para el usuario: con el cual un usuario podra interactuar
while True:
    print("\nBienvenido al Centro de Adopción Huellas en Bogota\n")
    print("\nElige una opción:\n")
    print("1. Mascotas disponibles para adopción")
    print("2. Buscar mascota según mis preferencias")
    print("3. Donaciones")
    print("4. Contáctanos")
    print("5. Salir")

    opcion = input("\nIngresa el número de tu opción: ")

    if opcion == "1":
     print("\nEstas son nuestras mascotas disponibles:")
    for mascota in lista_mascotas:
        print(f"- {mascota['nombre']} ({mascota['especie']}, {mascota['sexo']}, {mascota['edad_meses']} meses, {mascota['descripcion']})")

    desea_filtrar = input("\n¿Deseas filtrar las mascotas disponibles? (si/no): ").lower()

    lista_filtrada = lista_mascotas 

    if desea_filtrar == "si":
        especie = input("¿Qué especie deseas? (perro/gato): ").lower()
        sexo = input("¿Qué sexo deseas? (macho/hembra): ").lower()

        lista_filtrada = filtrar_mascotas(lista_mascotas, especie=especie, sexo=sexo)

        print("\nMascotas filtradas:")
        if lista_filtrada:
            for mascota in lista_filtrada:
                print(f"- {mascota['nombre']} ({mascota['especie']}, {mascota['sexo']})")
        else:
            print("No encontramos mascotas con esas características")
            lista_filtrada = []  # vacío si no hay coincidencias

    if lista_filtrada:  
        adoptar = input("\n¿Quieres adoptar alguna de estas mascotas? (si/no): ").lower()

        if adoptar == "si":
            nombre = input("Escribe el nombre de la mascota que quieres adoptar: ")

            encontrada = None
            for mascota in lista_filtrada:
                if mascota["nombre"].lower() == nombre.lower():
                    encontrada = mascota
                    break

            if encontrada:
                print(f"\nFelicitaciones, estás a un paso de cambiar la vida de {encontrada['nombre']}, nos pondremos en contacto contigo")
            else:
                print("\nLo sentimos, no encontramos una mascota con ese nombre.")
        else:
            print("\nPerfecto, volviendo al menú principal...")


    elif opcion == "2":
        print("\nIngresa tus preferencias para encontrar la mascota ideal")
        especie = input("Especie (perro/gato): ")
        tamano = input("Tamaño (pequeño/mediano/grande): ")
        sexo = input("Sexo (macho/hembra): ")
        con_ninos = input("¿Debe ser apto con niños? (si/no): ").lower() == "si"

        preferencias_usuario = {
            'especie': especie,
            'tamano': tamano,
            'sexo': sexo,
            'con_ninos': con_ninos
        }

        sugerencias = sugerir_mascotas(lista_mascotas, preferencias_usuario)

        print("\nMascotas sugeridas según tus preferencias:")
        for mascota, puntaje in sugerencias:
            print(f"- {mascota['nombre']} ({mascota['especie']}, {mascota['sexo']}) → Puntaje: {puntaje}")

    elif opcion == "3":
        print("\nGracias por tu interés en apoyar")
        print("Por ahora esta opción no está disponible.")

    elif opcion == "4":
        print("\nPuedes escribirnos al correo: santiago@adopcion.co")

    elif opcion == "5":
        print("\nBienvenido al Centro de Adopción Huellas en Bogota¡Hasta pronto!")
        break

    else:
        print("\nOpción inválida, por favor intenta de nuevo.")