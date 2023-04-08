const imagenPrincipal = document.querySelector('#imagen-principal');
const imagenesSecundarias = document.querySelectorAll('.imagen-secundaria');

imagenesSecundarias.forEach(imagen => {
  imagen.addEventListener('click', () => {
    const imagenSeleccionada = imagen.src;
    imagen.src = imagenPrincipal.src;
    imagenPrincipal.src = imagenSeleccionada;
  });
});

