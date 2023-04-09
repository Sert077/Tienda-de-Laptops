var fileUpload = document.querySelector('input[name="imagen_1"]')
var reader = new FileReader();
fileUpload.addEventListener('change', () => {
  reader.readAsDataURL(fileUpload.files[0]);
  reader.onload = (e) => {
    var image = new Image();
    image.src = e.target.result;
    image.onload = () => {
      var {
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
var fileUpload = document.querySelector('input[name="imagen_2"]')
var reader = new FileReader();
fileUpload.addEventListener('change', () => {
  reader.readAsDataURL(fileUpload.files[0]);
  reader.onload = (e) => {
    var image = new Image();
    image.src = e.target.result;
    image.onload = () => {
      var {
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
  var fileUpload = document.querySelector('input[name="imagen_3"]')
var reader = new FileReader();
fileUpload.addEventListener('change', () => {
  reader.readAsDataURL(fileUpload.files[0]);
  reader.onload = (e) => {
    var image = new Image();
    image.src = e.target.result;
    image.onload = () => {
      var {
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
  var fileUpload = document.querySelector('input[name="imagen_4"]')
var reader = new FileReader();
fileUpload.addEventListener('change', () => {
  reader.readAsDataURL(fileUpload.files[0]);
  reader.onload = (e) => {
    var image = new Image();
    image.src = e.target.result;
    image.onload = () => {
      var {
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
