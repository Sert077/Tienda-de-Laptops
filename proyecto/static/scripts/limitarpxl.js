
var fileUpload2 = document.querySelector('input[name="imagen_2"]')
var reader2 = new FileReader();
fileUpload2.addEventListener('change', () => {
  reader2.readAsDataURL(fileUpload2.files[0]);
  reader2.onload = (e) => {
    var image2 = new Image();
    image2.src = e.target.result;
    image2.onload = () => {
      var height2 = image2.height;
      var width2 = image2.width;
      console.log(height2+" "+width2);

      if (height2 < 1080 || width2 < 720) {

        fileUpload2.value = '';
        alert("La resolucion minima de la imagen debe ser 1080x720");
        return false;
      }
      alert("Imagen aceptada!");
      return true;
    };
  };})

  var fileUpload4 = document.querySelector('input[name="imagen_4"]')
var reader4 = new FileReader();
fileUpload4.addEventListener('change', () => {
  reader4.readAsDataURL(fileUpload4.files[0]);
  reader4.onload = (e) => {
    var image4 = new Image();
    image4.src = e.target.result;
    image4.onload = () => {
      var height4 = image4.height;
      var width4 = image4.width;
      console.log(height4 + " " + width4);

      if (height4 < 1080 || width4 < 720) {
        fileUpload4.value = '';

        alert("La resolucion minima de la imagen debe ser 1080x720");
        return false;
      }
      alert("Imagen aceptada!");
      return true;
    };
  };})
  

  var fileUpload3 = document.querySelector('input[name="imagen_3"]')
var reader3 = new FileReader();
fileUpload3.addEventListener('change', () => {
  reader3.readAsDataURL(fileUpload.files[0]);
  reader3.onload = (e) => {
    var image3 = new Image();
    image3.src = e.target.result;
    image3.onload = () => {
      var height3 = image3.height;
      var width3= image3.width;
      console.log(height3 + " " + width3);

      if (height3 < 1080 || width3 < 720) {

        fileUpload3.value = '';

        alert("La resolucion minima de la imagen debe ser 1080x720");
        return false;
      }
      alert("Imagen aceptada!");
      return true;
    };
  };})


  var fileUpload1 = document.querySelector('input[name="imagen_1"]')
var reader1 = new FileReader();
fileUpload1.addEventListener('change', () => {
  reader1.readAsDataURL(fileUpload1.files[0]);
  reader1.onload = (e) => {
    var image1 = new Image();
    image1.src = e.target.result;
    image1.onload = () => {
      var height1 = image1.height;
      var width1 = image1.width;
      console.log(height1 + " " + width1);

      if (height1 < 1080 || width1 < 720) {

        fileUpload1.value = '';

        alert("La resolucion minima de la imagen debe ser 1080x720");
        return false;
      }
      alert("Imagen aceptada!");
      return true;
    };
  };})
