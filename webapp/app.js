//Slider
var bar = document.getElementById("myRange");
var valueOutput = document.getElementById("value");

valueOutput.innerHTML = bar.ariaValueMax;
bar.oninput = function() {
    valueOutput.innerHTML = this.value;
}

//Counter
let add = document.getElementById("increment");
let subtract = document.getElementById("decrement");

let int = document.getElementById("number");
let integer = 0;

add.addEventListener("click", function(){
    integer += 1;
    int.innerHTML = integer;
})

subtract.addEventListener("click", function(){
    integer -= 1;
    int.innerHTML = integer;
})

//Counter2
let add2 = document.getElementById("increment2");
let subtract2 = document.getElementById("decrement2");

let int2 = document.getElementById("number2");
let integer2 = 0;

add2.addEventListener("click", function(){
    integer2 += 1;
    int2.innerHTML = integer2;
})

subtract2.addEventListener("click", function(){
    integer2 -= 1;
    int2.innerHTML = integer2;
})

