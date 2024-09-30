document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    const navItems = document.querySelectorAll('.navbar-nav .nav-link');

    // Mostrar solo la sección principal al cargar
    sections.forEach(section => {
        section.classList.remove('active'); // Oculta todas las secciones
    });
    document.getElementById('section1').classList.add('active'); // Muestra la sección principal

    // Cambiar de sección al hacer clic en los links
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault(); // Evitar el comportamiento por defecto de los enlaces
            const targetSection = e.target.getAttribute('data-target');

            // Ocultar todas las secciones
            sections.forEach(section => {
                section.classList.remove('active');
            });

            // Mostrar la sección seleccionada
            document.getElementById(targetSection).classList.add('active');

            // Cambiar la clase activa en la navbar
            navItems.forEach(navItem => {
                navItem.classList.remove('active');
            });
            e.target.classList.add('active');
        });
    });
});
