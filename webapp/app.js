var slider = document.getElementById("myRange");
var output = document.getElementById("value");

output.innerHTML = slider.ariaValueMax;
slider.oninput = function() {
    output.innerHTML = this.value;
}