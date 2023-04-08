const fileUpload = document.querySelector('input[type="file"]')
const reader = new FileReader();



fileUpload.addEventListener('change', () => {
  reader.readAsDataURL(fileUpload.files[0]);
  reader.onload = (e) => {
    const image = new Image();
    image.src = e.target.result;
    image.onload = () => {
      const {
        height,
        width
      } = image;
      if (height < 1080 || width < 720) {
        alert("La resolucion minima de la imagen debe ser 1080x720");
        return false;
      }
      alert("Imagen aceptada!");
      return true;
    };
  };})

()

 