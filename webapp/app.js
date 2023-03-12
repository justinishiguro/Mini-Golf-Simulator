//Slider
var slider = document.getElementById("myRange");
var output = document.getElementById("value");

output.innerHTML = slider.ariaValueMax;
slider.oninput = function() {
    output.innerHTML = this.value;
}

//Counter
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

//Counter2
let add2 = document.getElementById("increment2");
let subtract2 = document.getElementById("decrement2");

let int2 = document.getElementById("number2");
let integer2 = 0;

add2.addEventListener("click", function(){
    integer2++;
    int2.innerHTML = integer2;
})

subtract2.addEventListener("click", function(){
    integer2--;
    int2.innerHTML = integer2;
})