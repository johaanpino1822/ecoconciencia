from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_charts():
    return render_template('GraficosP.html')

# Leer el archivo CSV
df = pd.read_csv('Fuentes_Electricas.csv')           
print(df['Valores'])    

# Calcular el porcentaje de participación de cada fuente
total_generacion = df['Valores'].sum()
df['Porcentaje'] = (df['Valores'] / total_generacion) * 100

# Calcular la media
media = df['Valores'].mean()

# Crear el gráfico de barras
fig, ax = plt.subplots()
ax.bar(df['FuentesdeEnergia'], df['Valores'], color=['blue', 'green', 'yellow', 'brown'])

# Añadir una línea horizontal para la media
ax.axhline(y=media, color='red', linestyle='--', label=f'Media: {media:.1f}')

# Configurar el título y las etiquetas
ax.set_title('Fuentes de Generación eléctrica, Colombia, 2023')
ax.set_xlabel('Fuentes de Energia')
ax.set_ylabel('Valores')

# Añadir los porcentajes encima de cada barra
for index, value in enumerate(df['Valores']):
    porcentaje = df['Porcentaje'][index]
    ax.text(index, value + 200, f'{porcentaje:.1f}%', ha='center', fontsize=10)

# Añadir leyenda
ax.legend()


plt.savefig('static/fuentes_barras.png')
plt.close(fig)


if __name__ == "__main__":
    app.run(debug=True)
    

