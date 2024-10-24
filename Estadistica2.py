from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_charts():
    return render_template('index.html')

df = pd.read_csv('Fuentes_Renovables.csv', delimiter=';')

# Calcular las medias
Datos_wind = df['wind'].mean()   ##Extraer los datos de la columnasy calcula la media o promedio 
Datos_hydro = df['hydro'].mean()
Datos_solar = df['solar'].mean()
Datos_bio = df['Other renewables including bioenergy'].mean()

# Crear el gráfico de barras
fig1, ax = plt.subplots()

Valores= [Datos_wind, Datos_hydro, Datos_solar, Datos_bio] ## se crear una variable para almacenar todas las variables en una sola en este caso para valores por cada items
Fuentes = ['Wind', 'Hydro', 'Solar', 'Bioenergy']



colores_personalizados = ['#13f310', '#1032f3', '#641e16', '#f310d4'] #colores de las fuentes
explode = (0.4, 0.2, 0.6, 1.2)  # Separación para cada segmento del gráfico 


# Generar el gráfico de torta con más personalización
ax.pie(
    Valores, 
    labels=Fuentes, 
    autopct='%1.1f%%', 
    colors=colores_personalizados,  # Aplicar los colores personalizados
    startangle=0.85, 
    explode=explode,  # Separar los segmentos
    pctdistance=0.90,  # Distancia de los porcentajes al centro
    labeldistance=1.07,  # Ajuste de distancia de las etiquetas
    shadow=True,  # Agregar una sombra
    textprops={'fontsize': 7}  # Ajustar el tamaño del texto de las etiquetas
)
# Añadir título a la gráfica
plt.title('Producción de Energia por fuente renovable (prom. 2004-2021)', fontsize=10)
ax.axis('equal')  # Asegura que el gráfico sea circular

plt.savefig('static/fuentes_torta.png')
plt.close(fig1)










