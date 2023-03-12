var slider = document.getElementById("myRange");
var output = document.getElementById("value");

output.innerHTML = slider.ariaValueMax;
slider.oninput = function() {
    output.innerHTML = this.value;
}

let add = document.getElementById("increment");
let subtract = document.getElementById("decrement");

let int = document.getElementById("number");
let integer = 0;

add.addEventListener("click", function(){
    integer++;
    int.innerHTML = integer;
})

subtract.addEventListener("click", function(){
    integer--;
    int.innerHTML = integer;
})