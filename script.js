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