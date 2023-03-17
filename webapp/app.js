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

let which_key = "NULL";
document.addEventListener("keydown", function(event) {
    which_key = event.key;
    if(which_key == "ArrowLeft"){
        if(integer2 <= 20 && integer2 > -20){
            integer2 -= 1;
            }
        int2.innerHTML = integer2;
    }

    else if(which_key == "ArrowDown"){
        if(integer <= 20 && integer > -20){
            integer -= 1;
        }
        int.innerHTML = integer;
    }
    
    else if(which_key == "ArrowUp"){
        if(integer < 20 && integer >= -20){
            integer += 1;
        }
        int.innerHTML = integer;
    }

    else if(which_key == "ArrowRight"){
        if(integer2 < 20 && integer2 >= -20){
            integer2 += 1;
        }
        int2.innerHTML = integer2;
    }
    else if(which_key == "r"){
        integer = 0;
        integer2 = 0;
        int.innerHTML = 0;
        int2.innerHTML = 0;
    }
    else;
});


document.addEventListener("keydown", function(event) {
    if(event.key == "ArrowUp" || event.key == "ArrowDown" || event.key == "ArrowLeft" || event.key == "ArrowRight"){
        event.preventDefault();
    }
})

document.addEventListener("keydown", function(event){
    if(event.key == 'q'){
        window.location.href = "http://127.0.0.1:5500/index.html";
    }
})