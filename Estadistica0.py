from flask import Flask, render_template, url_for
import matplotlib.pyplot as plt
import pandas as pd
import os

app = Flask(__name__)

# Ruta principal que muestra todos los gráficos directamente
@app.route('/')
def index():
    # Leer el archivo CSV (puedes cambiarlo si usas otros archivos para los otros gráficos)
    df = pd.read_csv('Fuentes_Electricas.csv')

    # --- Gráfico de Barras ---
    fig_barras, ax_barras = plt.subplots()
    ax_barras.bar(df['FuentesdeEnergia'], df['Valores'], color=['blue', 'green', 'yellow', 'brown'])
    ax_barras.set_title('Fuentes de Generación eléctrica, Colombia, 2023')
    ax_barras.set_xlabel('Fuentes de Energía')
    ax_barras.set_ylabel('Valores')
    plt.savefig(os.path.join('static', 'fuentes_barras.png'))
    plt.close(fig_barras)

    # --- Gráfico de Torta ---
    fig_torta, ax_torta = plt.subplots()
    ax_torta.pie(df['Valores'], labels=df['FuentesdeEnergia'], autopct='%1.1f%%', colors=['blue', 'green', 'yellow', 'brown'])
    ax_torta.set_title('Distribución de Fuentes de Energía')
    plt.savefig(os.path.join('static', 'fuentes_torta.png'))
    plt.close(fig_torta)

    # --- Gráfico de Líneas ---
    fig_lineas, ax_lineas = plt.subplots()
    ax_lineas.plot(df['FuentesdeEnergia'], df['Valores'], marker='o')
    ax_lineas.set_title('Tendencia de Generación Eléctrica')
    ax_lineas.set_xlabel('Fuentes de Energía')
    ax_lineas.set_ylabel('Valores')
    plt.savefig(os.path.join('static', 'fuentes_lineas.png'))
    plt.close(fig_lineas)

    # --- Gráfico de Área ---
    fig_area, ax_area = plt.subplots()
    ax_area.fill_between(df['FuentesdeEnergia'], df['Valores'], color='skyblue', alpha=0.4)
    ax_area.set_title('Gráfico de Área - Generación Eléctrica')
    ax_area.set_xlabel('Fuentes de Energía')
    ax_area.set_ylabel('Valores')
    plt.savefig(os.path.join('static', 'grafico_area.png'))
    plt.close(fig_area)

    # Renderiza la plantilla y envía las imágenes
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
