document.addEventListener('DOMContentLoaded', () => {
    // Seleccionar elementos del DOM
    const sections = document.querySelectorAll('.section');
    const navItems = document.querySelectorAll('.navbar-nav .nav-link');
    const defaultSectionId = 'section1';
  
    // Función para mostrar una sección específica
    const mostrarSeccion = (idSeccion) => {
      sections.forEach(section => section.classList.remove('active'));
      const seccionObjetivo = document.getElementById(idSeccion);
      if (seccionObjetivo) {
        seccionObjetivo.classList.add('active');
      } else {
        console.error(`Sección con id "${idSeccion}" no encontrada`);
      }
    };
  
    // Función para actualizar el estado activo en la navegación
    const actualizarEstadoNavegacionActiva = (elementoClicado) => {
      navItems.forEach(item => item.classList.remove('active'));
      elementoClicado.classList.add('active');
    };
  
    // Mostrar la sección por defecto al cargar
    mostrarSeccion(defaultSectionId);
  
    // Usar delegación de eventos para mejor rendimiento
    document.querySelector('.navbar-nav').addEventListener('click', (e) => {
      const elementoNav = e.target.closest('.nav-link');
      if (elementoNav) {
        e.preventDefault();
        const idSeccionObjetivo = elementoNav.getAttribute('data-target');
        if (idSeccionObjetivo) {
          mostrarSeccion(idSeccionObjetivo);
          actualizarEstadoNavegacionActiva(elementoNav);
          desplazamientoSuave(idSeccionObjetivo); // Activar desplazamiento suave
        } else {
          console.error('Atributo data-target falta en el elemento de navegación');
        }
      }
    });
  
    // Función para desplazamiento suave
    const desplazamientoSuave = (idObjetivo) => {
      const elementoObjetivo = document.getElementById(idObjetivo);
      if (elementoObjetivo) {
        elementoObjetivo.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };
  
    // Actualizar sección activa al desplazarse (opcional)
    const opcionesObservador = {
      root: null,
      rootMargin: '0px',
      threshold: 0.7,
    };
  
    const callbackObservador = (entradas) => {
      entradas.forEach(entrada => {
        if (entrada.isIntersecting) {
          const idIntersectando = entrada.target.id;
          actualizarEstadoNavegacionActiva(document.querySelector(`.nav-link[data-target="${idIntersectando}"]`));
        }
      });
    };
  
    const observador = new IntersectionObserver(callbackObservador, opcionesObservador);
    sections.forEach(section => observador.observe(section));
  
    // Agregar manejo de errores global
    window.addEventListener('error', (evento) => {
      console.error('Error capturado:', evento.error.message);
      // Aquí puedes agregar lógica adicional para manejar errores, como mostrar un mensaje al usuario
    });
  
    console.log('Navegación de secciones inicializada con éxito');
  });
  
  // Simulación de estructura DOM para demostración
  const mockDOM = `
    <nav class="navbar-nav">
      <a class="nav-link" data-target="section1" href="#">Sección 1</a>
      <a class="nav-link" data-target="section2" href="#">Sección 2</a>
    </nav>
    <div id="section1" class="section">Contenido de la Sección 1</div>
    <div id="section2" class="section">Contenido de la Sección 2</div>
  `;
  
