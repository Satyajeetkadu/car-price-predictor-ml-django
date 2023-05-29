function load_car_models() {
    var companySelect = document.getElementById("company");
    var carModelSelect = document.getElementById("car_models");
    var selectedCompany = companySelect.value;

    // Clear existing options
    carModelSelect.innerHTML = "";

    // Get the car models JSON script element
    var carModelsScript = document.getElementById("carModelsData");
    var carModelsJSON = JSON.parse(carModelsScript.textContent || carModelsScript.innerText);

    // Filter car models based on the selected company
    for (var i = 0; i < carModelsJSON.length; i++) {
        if (carModelsJSON[i].company === selectedCompany) {
            var models = carModelsJSON[i].models;
            for (var j = 0; j < models.length; j++) {
                var option = document.createElement("option");
                option.text = models[j];
                option.value = models[j];
                carModelSelect.appendChild(option);
            }
        }
    }
}



function form_handler(event) {

console.log("data sent")
event.preventDefault();
console.log("Form submitted!"); // Don't submit the form normally

var fd = new FormData(document.querySelector('form'));
var xhr = new XMLHttpRequest({ mozSystem: true });

xhr.open('POST', '/predict/predicted_price/', true);
document.getElementById('prediction').innerHTML = "Wait! Predicting Price.....";
xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        var response = JSON.parse(xhr.responseText);
        document.getElementById('prediction').innerHTML = "Prediction: ₹" + response.predicted_price;
    }
};

xhr.onload = function () { };

xhr.send(fd);
}



document.addEventListener("DOMContentLoaded", function () {
var form = document.querySelector('form');
form.addEventListener("submit", form_handler);

var companySelect = document.getElementById("company");
companySelect.addEventListener("change", load_car_models);
});

  