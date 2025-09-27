import pandas as pd
import matplotlib.pyplot as plt

# --- DATOS DANE ---
datos = {
    'Año': [2018, 2019, 2020, 2021, 2022],
    'Bogotá': [7830, 7900, 7970, 8050, 8120],
    'Antioquia': [6420, 6480, 6535, 6590, 6645],
    'Valle del Cauca': [4840, 4900, 4955, 5020, 5090]
}

df = pd.DataFrame(datos)

# --- FUNCIONES ---
def tasa_crecimiento(valor_inicial, valor_final, años):
    return (valor_final / valor_inicial) ** (1/años) - 1

def calcular_tasas(df):
    tasas = {}
    for region in ['Bogotá', 'Antioquia', 'Valle del Cauca']:
        valor_inicial = df[region].iloc[0]
        valor_final = df[region].iloc[-1]
        años = df['Año'].iloc[-1] - df['Año'].iloc[0]
        tasas[region] = tasa_crecimiento(valor_inicial, valor_final, años)
    return tasas

def proyectar(df, tasas, años_proyeccion=5):
    ultimo_año = df['Año'].iloc[-1]
    proyeccion = pd.DataFrame({'Año': [ultimo_año + i for i in range(1, años_proyeccion+1)]})
    for region in ['Bogotá', 'Antioquia', 'Valle del Cauca']:
        ultimo_valor = df[region].iloc[-1]
        tasa = tasas[region]
        proyeccion[region] = [ultimo_valor * (1 + tasa) ** i for i in range(1, años_proyeccion+1)]
    return proyeccion

def graficar(df, proyeccion):
    plt.figure(figsize=(10,6))
    for region in ['Bogotá', 'Antioquia', 'Valle del Cauca']:
        plt.plot(df['Año'], df[region], marker='o', label=f'{region} (histórico)')
        plt.plot(proyeccion['Año'], proyeccion[region], marker='x', linestyle='--', label=f'{region} (proyección)')
    plt.title('Crecimiento poblacional por regiones y proyección a 5 años')
    plt.xlabel('Año')
    plt.ylabel('Población (miles)')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- MENÚ PRINCIPAL ---
tasas = calcular_tasas(df)
proyeccion_df = proyectar(df, tasas)

while True:
    print("\n" + "BIENVENIDO AL DANE".center(60, " "))
    print("\nA continuación podrás visualizar los datos de crecimiento poblacional por regiones.\n")
    
    print("Datos históricos:")
    print(df.to_string(index=False))
    
    print("\nProyección para los próximos 5 años:")
    print(proyeccion_df.to_string(index=False))
    
    opcion = input("\n¿Deseas ver la gráfica de la proyección? (Sí/No) ").strip().lower()
    
    if opcion == 'sí' or opcion == 'si':
        graficar(df, proyeccion_df)
        input("Presiona Enter para regresar al menú principal...")
    elif opcion == 'no':
        print("\nRegresando al menú principal...\n")
    else:
        print("\nOpción no reconocida. Intenta de nuevo.\n")
