document.addEventListener('DOMContentLoaded', () => {
    // Seleccionar elementos del DOM
    const sections = document.querySelectorAll('.section');
    const navItems = document.querySelectorAll('.navbar-nav .nav-link');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    // Función para mostrar una sección específica
    const mostrarSeccion = (idSeccion) => {
        sections.forEach(section => {
            if (section.id === idSeccion) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });
    };

    // Función para actualizar el estado activo en la navegación
    const actualizarEstadoNavegacionActiva = (elementoClicado) => {
        navItems.forEach(item => item.classList.remove('active'));
        elementoClicado.classList.add('active');
    };

    // Manejar clics en la navegación
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('data-target');
            if (targetId) {
                mostrarSeccion(targetId);
                actualizarEstadoNavegacionActiva(item);
                
                // Desplazamiento suave a la sección
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }

                // Cerrar el menú de navegación en móviles
                if (window.innerWidth < 992 && navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            }
        });
    });

    // Mostrar la sección inicial
    mostrarSeccion('section1');

    console.log('Navegación de secciones inicializada con éxito');
});

// Función para realizar los cálculos de porcentajes energéticos
function calcular() {
    let num = parseInt(document.getElementById('Ninput').value);

    let resultado1 = num * 0.668;
    let resultado2 = num * 0.0148;
    let resultado3 = num * 0.001;
    let resultado4 = num * 0.0112;
    let resultado5 = num * 0.3050;

    document.getElementById('resultado1').textContent = 'El porcentaje Hidráulico es ' + resultado1.toFixed(2) + ' kW/h';
    document.getElementById('resultado2').textContent = 'El porcentaje Solar es ' + resultado2.toFixed(2) + ' kW/h';
    document.getElementById('resultado3').textContent = 'El porcentaje Eólica es ' + resultado3.toFixed(2) + ' kW/h';
    document.getElementById('resultado4').textContent = 'El porcentaje Biomasa es ' + resultado4.toFixed(2) + ' kW/h';
    document.getElementById('resultado5').textContent = 'El porcentaje Combustible fósil y Energía térmica es ' + resultado5.toFixed(2) + ' kW/h';
}

document.addEventListener('DOMContentLoaded', function () {
  let Filas = [];
  const Paises = new Set();
  const CuerpoTbla = document.querySelector('#datosTabla tbody');
  const FiltroPais = document.getElementById('FiltroPais');

  // Fetch para obtener el contenido del archivo CSV
  fetch('./datosM.csv')
    .then(response => response.text())
    .then(data => {
      // Dividir el texto del CSV en filas (cada línea es una fila)
      Filas = data.split('\n');

      // Llenar el conjunto de países y cargar el select
      Filas.forEach((row, index) => {
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
  function filtrarTabla() {
    // Obtener el valor seleccionado en el filtro
    const filtro = FiltroPais.value;

    // Limpiar el contenido de la tabla
    CuerpoTbla.innerHTML = '';

    // Crear un fragmento de documento para insertar filas filtradas
    const fragmento = document.createDocumentFragment();

    // Filtrar y mostrar las filas que coinciden con el país seleccionado
    Filas.forEach((row, index) => {
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

    // Insertar las filas filtradas en el DOM
    CuerpoTbla.appendChild(fragmento);
  }

  // Llamar a filtrarTabla cuando se cambie el select del filtro
  FiltroPais.addEventListener('change', filtrarTabla);
});

document.addEventListener('DOMContentLoaded', function() {
  // Cargar el contenido de graficosLineas.html al cargar la página
  fetch('/grafico')
      .then(response => response.text())
      .then(data => {
          // Insertar el contenido en el div con id "grafico"
          document.getElementById('grafico').innerHTML = data;
      })
      .catch(error => console.error('Error al cargar el gráfico:', error));
});

