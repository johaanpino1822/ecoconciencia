from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
@app.route('/')
def show_charts():
     return render_template('index.html')  #l gráfico es generado cuando visitas la ruta '/', y después se renderiza el template 'graficosP.html'.
    
    # Leer el archivo CSV de energía renovable
df_renovable = pd.read_csv('Emissions_CO2.csv')
    
    
    
# Asegurarse de que los años están en el formato adecuado (ej. columna 'Year')
años = df_renovable['Year']
valores = df_renovable['value']

    # Calcular la media
media_renovable = valores.mean()

    # Calcular la desviación estándar
std_renovable = valores.std()

 # Imprimir la media y desviación estándar 
print(f'Media: {media_renovable}, Desviación estándar: {std_renovable}')


    # Crear el gráfico de área
fig, ax = plt.subplots()##fig representa la figura, que es el contenedor general para todo el gráfico, y ax representa los ejes, que es donde se colocan los gráficos específicos (líneas, barras, etc.).

    # Graficar las emisiones (linea)
ax.fill_between(años,valores, color='green', label='Emisiones',alpha=0.4)


    # Graficar las medias
ax.plot(años, valores, color='green', label='Emisiones')

# Mostrar la media como una línea horizontal (opcional)
ax.axhline(y=media_renovable, color='red', linestyle='--', label=f'Media ({media_renovable:.2f})')

# Anotación en el gráfico con el valor de la desviación estándar
    # Se ajusta para que no quede fuera de la gráfica
ax.text(años.iloc[-10], media_renovable + std_renovable, f'Desviación estándar: {std_renovable:.2f}', 
            color='blue', fontsize=10, verticalalignment='bottom', horizontalalignment='right')




    # Configuración del gráfico
ax.set_title('Emisiones de CO2 por Combustibles Fósiles, Colombia (2000-2022)')
ax.set_xlabel('Año')
ax.set_ylabel('valor')
ax.legend()

# Líneas para la desviación estándar (media + std, media - std)
ax.axhline(y=media_renovable + std_renovable, color='blue', linestyle='--', label=f'Media + 1 std ({media_renovable + std_renovable:.2f})')
ax.axhline(y=media_renovable - std_renovable, color='blue', linestyle='--', label=f'Media - 1 std ({media_renovable - std_renovable:.2f})')

    # Guardar el gráfico en la carpeta static
plt.savefig('static/grafico_area.png') #El gráfico se guarda en la carpeta static para que pueda ser accedido desde la página HTML.
plt.close(fig)

if __name__ == "__main__":
    app.run(debug=True)
    