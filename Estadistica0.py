from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza la plantilla principal
    return render_template('index.html')

@app.route('/index.html')
def indexDos():
    # Renderiza la plantilla principal
    return render_template('index.html')

@app.route('/medicion.html')
def medicion():
    return render_template('medicion.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/soluciones.html')
def soluciones():
    # Renderiza la plantilla principal
    return render_template('soluciones.html')


# Leer los archivos CSV
df = pd.read_csv('Fuentes_Electricas.csv', delimiter=',')
df1 = pd.read_csv('Fuentes_Renovables.csv', delimiter=';')
df2 = pd.read_csv('Evolucion_Fuentes.csv', delimiter=',')
df3 = pd.read_csv('Emissions_CO2.csv', delimiter=',')

# Verificar columnas del archivo Evolucion_Fuentes.csv
print("Columnas en Evolucion_Fuentes.csv:", df2.columns)

if 'Fuentes' not in df2.columns:
    raise KeyError("La columna 'Fuentes' no existe en Evolucion_Fuentes.csv. Verifica el archivo CSV y el nombre de las columnas.")

# Gráfico de barras
total_generacion = df['Valores'].sum()
df['Porcentaje'] = (df['Valores'] / total_generacion) * 100
media = df['Valores'].mean()

fig, ax = plt.subplots()
ax.bar(df['FuentesdeEnergia'], df['Valores'], color=['blue', 'green', 'yellow', 'brown'])
ax.axhline(y=media, color='red', linestyle='--', label=f'Media: {media:.1f}')
ax.set_title('Fuentes de Generación eléctrica, Colombia, 2023')
ax.set_xlabel('Fuentes de Energia')
ax.set_ylabel('Valores')

for index, value in enumerate(df['Valores']):
    porcentaje = df['Porcentaje'][index]
    ax.text(index, value + (0.01 * value), f'{porcentaje:.1f}%', ha='center', fontsize=10)

# Añadir leyenda
ax.legend()
plt.savefig('static/fuentes_barras.png')
plt.close(fig)

# Gráfico de tortas
Datos_wind = df1['wind'].mean()
Datos_hydro = df1['hydro'].mean()
Datos_solar = df1['solar'].mean()
Datos_bio = df1['Other renewables including bioenergy'].mean()
fig1, ax = plt.subplots()

Valores = [Datos_wind, Datos_hydro, Datos_solar, Datos_bio]
Fuentes = ['Wind', 'Hydro', 'Solar', 'Bioenergy']

colores_personalizados = ['#13f310', '#1032f3', '#641e16', '#f310d4']
explode = (0.4, 0.2, 0.6, 1.2)

ax.pie(Valores, labels=Fuentes, autopct='%1.1f%%', colors=colores_personalizados, startangle=0.85, explode=explode, pctdistance=0.90, labeldistance=1.07, shadow=True, textprops={'fontsize': 10})
plt.title('Producción de Energia por fuente renovable (promedio del 2004-2021)', fontsize=14)
ax.axis('equal')

plt.savefig('static/fuentes_torta.png')
plt.close(fig1)

# Gráfico de Líneas
df.dropna(inplace=True)
fig2, ax = plt.subplots(figsize=(10, 6))

for fuente in df2['Fuentes'].unique():
    subset = df2[df2['Fuentes'] == fuente]
    ax.plot(subset['Year'], subset['Value'], label=fuente)
    mediana = subset['Value'].median()
    ax.axhline(y=mediana, linestyle='--', alpha=0.6)
    ax.text(subset['Year'].iloc[-1] + 0.5, mediana, f'Mediana {fuente}: {int(mediana)} GWh', fontsize=9, verticalalignment='center')

  # Leyenda
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Mover la leyenda fuera del gráfico
ax.set_ylim(0, 80000)
plt.xlabel('Años')
plt.ylabel('(GWh)')
plt.title('Evolución de las fuentes de generación eléctrica, Colombia 2000-2023')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1000)}k GWh'))
plt.legend()

plt.savefig('static/fuentes_lineas.png')
plt.close(fig2)

# Gráfico de Áreas
años = df3['Year']
valores = df3['value']

media_renovable = valores.mean()
std_renovable = valores.std()

fig3, ax = plt.subplots()
ax.fill_between(años, valores, color='green', label='Emisiones', alpha=0.4)
ax.plot(años, valores, color='green', label='Emisiones')
ax.axhline(y=media_renovable, color='red', linestyle='--', label=f'Media ({media_renovable:.2f})')
ax.text(años.iloc[-10], media_renovable + std_renovable, f'Desviación estándar: {std_renovable:.2f}', color='blue', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

ax.set_title('Emisiones de CO2 por Combustibles Fósiles, Colombia (2000-2022)')
ax.set_xlabel('Año')
ax.set_ylabel('valor')
ax.legend()

ax.axhline(y=media_renovable + std_renovable, color='blue', linestyle='--', label=f'Media + 1 std ({media_renovable + std_renovable:.2f})')
ax.axhline(y=media_renovable - std_renovable, color='blue', linestyle='--', label=f'Media - 1 std ({media_renovable - std_renovable:.2f})')

plt.savefig('static/grafico_area.png')
plt.close(fig3)

if __name__ == "__main__":
    app.run(debug=True)
