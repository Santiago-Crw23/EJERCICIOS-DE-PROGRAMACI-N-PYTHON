# ==============================
# 1ra parte: Estructura inicial
# ==============================

# Diccionario para almacenar los productos
inventario = {}

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio unitario: "))

    if nombre in inventario:
        # Si el producto ya existe, actualizamos la cantidad
        inventario[nombre]["cantidad"] += cantidad
        inventario[nombre]["precio"] = precio  # Actualizamos el precio
        print(f"Producto '{nombre}' actualizado en el inventario.")
    else:
        # Si no existe, lo agregamos
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"Producto '{nombre}' registrado en el inventario.")


# ==============================
# 2da parte: Mostrar inventario
# ==============================

def mostrar_inventario():
    if not inventario:  # Si está vacío
        print("El inventario está vacío.")
    else:
        print("\n--- Inventario ---")
        print(f"{'Producto':<15}{'Cantidad':<10}{'Precio Unitario':<15}")
        print("-" * 40)
        for nombre, datos in inventario.items():
            print(f"{nombre:<15}{datos['cantidad']:<10}{datos['precio']:<15.2f}")


# ==============================
# 3ra parte: Calcular valor total
# ==============================

def calcular_valor_total():
    if not inventario:
        print("El inventario está vacío.")
    else:
        total = 0
        for datos in inventario.values():
            total += datos["cantidad"] * datos["precio"]
        print(f"El valor total del inventario es: ${total:.2f}")


# ==============================
# 4ta parte: Buscar producto
# ==============================

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").capitalize()
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"Producto encontrado: {nombre}")
        print(f"   Cantidad: {datos['cantidad']}")
        print(f"   Precio unitario: ${datos['precio']:.2f}")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


# ==============================
# 5ta parte: Registrar venta
# ==============================

def registrar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ").capitalize()
    if nombre not in inventario:
        print(f"El producto '{nombre}' no existe en el inventario.")
        return
    
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
    
    if cantidad_vendida > inventario[nombre]["cantidad"]:
        print(f"No hay suficiente stock. Disponible: {inventario[nombre]['cantidad']}")
    else:
        inventario[nombre]["cantidad"] -= cantidad_vendida
        print(f"Venta registrada. Stock actual de '{nombre}': {inventario[nombre]['cantidad']}")


# ==============================
# Menú principal
# ==============================

def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Calcular valor total")
        print("4. Buscar producto")
        print("5. Registrar venta")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_valor_total()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Programa principal
menu()
