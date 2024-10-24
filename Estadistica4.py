from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
@app.route('/')
def show_charts():
     return render_template('GraficosP.html')
    
    # Leer el archivo CSV de energía renovable
df_renovable = pd.read_csv('Emissions_CO2.csv')
    
    
    
# Asegurarse de que los años están en el formato adecuado (ej. columna 'Year')
años = df_renovable['Year']
valores = df_renovable['value']

    # Calcular la media
media_renovable = valores.mean()

    # Calcular la desviación estándar
std_renovable = valores.std()

    # Crear el gráfico de área
fig, ax = plt.subplots()

    # Graficar el área para energía renovable
ax.fill_between(años, media_renovable - std_renovable, media_renovable + std_renovable, 
                    color='green', alpha=0.2, label='Desviación estándar CO2')

    # Graficar las medias
ax.plot(años, valores, color='green', label='Consumo Renovable')

    # Configuración del gráfico
ax.set_title('Emisiones de CO2 por Combustibles Fósiles, Colombia (2000-2022)')
ax.set_xlabel('Año')
ax.set_ylabel('Valor')
ax.legend()


    # Guardar el gráfico en la carpeta static
plt.savefig('static/grafico_area.png')
plt.close(fig)

if __name__ == "__main__":
    app.run(debug=True)
    