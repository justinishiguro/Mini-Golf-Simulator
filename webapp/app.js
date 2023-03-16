//Slider
var bar = document.getElementById("myRange");
var valueOutput = document.getElementById("value");

valueOutput.innerHTML = bar.ariaValueMax;
bar.oninput = function() {
    valueOutput.innerHTML = this.value;
}

//Counter
let add = document.getElementById("increment1");
let subtract = document.getElementById("decrement1");

let int = document.getElementById("number");
let integer = 0;

add.addEventListener("click", function(){
    if(integer < 20 && integer >= -20){
        integer += 1;
    }
    int.innerHTML = integer;
    // console.log(integer);
})

subtract.addEventListener("click", function(){
    if(integer <= 20 && integer > -20){
        integer -= 1;
    }
    int.innerHTML = integer;
    // console.log(integer);
})

//Counter2
let add2 = document.getElementById("increment2");
let subtract2 = document.getElementById("decrement2");

let int2 = document.getElementById("number2");
let integer2 = 0;

add2.addEventListener("click", function(){
    if(integer2 < 20 && integer2 >= -20){
        integer2 += 1;
    }
    int2.innerHTML = integer2;
    // console.log(integer2);
})

subtract2.addEventListener("click", function(){
    if(integer2 <= 20 && integer2 > -20){
    integer2 -= 1;
    }
    int2.innerHTML = integer2;
    // console.log(integer2);
})

