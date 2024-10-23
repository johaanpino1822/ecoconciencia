from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/grafico')
def grafico():
    return render_template('graficosLineas.html')

@app.route('/plot.png')
def plot_png():
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [10, 20, 30, 40, 50]

    fig, ax = plt.subplots()
    ax.bar(categorias, valores)

    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_title('Gráfico de Barras')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
