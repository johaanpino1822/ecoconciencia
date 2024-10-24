from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd


app = Flask(__name__)

@app.route('/')
def show_charts():
    return render_template('index.html')

# Leer el archivo CSV
df = pd.read_csv('Evolucion_Fuentes.csv')

# Eliminar filas con valores faltantes (opcional)
df.dropna(inplace=True)


# Crear un gráfico de líneas
fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño del gráfico

# Agrupar datos por fuente y graficar
for fuente in df['Fuentes'].unique():
    subset = df[df['Fuentes'] == fuente]
    ax.plot(subset['Year'], subset['Value'], label=fuente)

# Calcular y mostrar la mediana
    mediana = subset['Value'].median()
    ax.axhline(y=mediana, linestyle='--', alpha=0.3)  # Añadir la línea de mediana en el gráfico
    # Añadir el texto de la mediana al lado de la línea
   
    ##Añadir el texto de la mediana con un pequeño desplazamiento vertical para evitar solapamientos
    ax.text(subset['Year'].iloc[-1] + 0.5, mediana , f'Mediana {fuente}: {int(mediana)} GWh', 
             fontsize=5, verticalalignment='center')



# Ajustar el límite del eje y
ax.set_ylim(0, 80000)

# Añadir etiquetas y título
plt.xlabel('Años')
plt.ylabel('(GWh)')
plt.title('Evolución de fuentes de generación eléctrica,Colombia/2000-2023')

# Ajustar el formato de los números en el eje y
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1000)}k GWh'))

# Añadir la leyenda
plt.legend()


# Guardar el gráfico en la carpeta 'static'
plt.savefig('static/fuentes_lineas.png')
plt.close(fig)


if __name__ == "__main__":
    app.run(debug=True)
    
