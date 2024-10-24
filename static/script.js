document.addEventListener('DOMContentLoaded', () => {
  // Función para calcular porcentajes energéticos
  function calcular() {
      const num = parseInt(document.getElementById('Ninput').value);
      const resultados = [
          num * 0.668,
          num * 0.0148,
          num * 0.001,
          num * 0.0112,
          num * 0.3050,
      ];
      const resultadosTextos = [
          'El porcentaje Hidráulico es ',
          'El porcentaje Solar es ',
          'El porcentaje Eólica es ',
          'El porcentaje Biomasa es ',
          'El porcentaje Combustible fósil y Energía térmica es ',
      ];
      resultados.forEach((resultado, index) => {
          document.getElementById(`resultado${index + 1}`).textContent = resultadosTextos[index] + resultado.toFixed(2) + ' kW/h';
      });
  }

  // Cargar datos de la tabla y manejar el filtrado
  const cargarDatosTabla = () => {
      const Paises = new Set();
      const CuerpoTbla = document.querySelector('#datosTabla tbody');
      const FiltroPais = document.getElementById('FiltroPais');

      fetch('./datosM.csv')
          .then(response => response.text())
          .then(data => {
              const filas = data.split('\n');
              filas.forEach((row, index) => {
                  const cols = row.split(',');
                  if (cols.length > 1 && index > 0) {
                      Paises.add(cols[0]); // Asumimos que el país está en la primera columna
                  }
              });

              // Llenar el select con las opciones de países
              Paises.forEach(country => {
                  const opcion = document.createElement('option');
                  opcion.value = country;
                  opcion.textContent = country;
                  FiltroPais.appendChild(opcion);
              });
          });

      // Función para filtrar la tabla según el país seleccionado
      FiltroPais.addEventListener('change', () => {
          const filtro = FiltroPais.value;
          CuerpoTbla.innerHTML = ''; // Limpiar el contenido de la tabla
          fetch('./datosM.csv')
              .then(response => response.text())
              .then(data => {
                  const filas = data.split('\n');
                  const fragmento = document.createDocumentFragment();
                  filas.forEach((row, index) => {
                      const cols = row.split(',');
                      if (cols.length > 1 && cols[0] === filtro) {
                          const ft = document.createElement('tr');
                          cols.forEach(col => {
                              const ct = document.createElement('td');
                              ct.textContent = col;
                              ft.appendChild(ct);
                          });
                          fragmento.appendChild(ft);
                      }
                  });
                  CuerpoTbla.appendChild(fragmento);
              });
      });
  };

  // Cargar los datos de la tabla
  cargarDatosTabla();

  // Cargar el contenido de graficosLineas.html al cargar la página
  fetch('/grafico')
      .then(response => response.text())
      .then(data => {
          document.getElementById('grafico').innerHTML = data;
      })
      .catch(error => console.error('Error al cargar el gráfico:', error));
});
