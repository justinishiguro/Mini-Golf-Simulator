//Slider
var bar = document.getElementById("myRange");
var valueOutput = document.getElementById("value");

valueOutput.innerHTML = bar.ariaValueMax;
bar.oninput = function() {
    valueOutput.innerHTML = this.value;
}

//Counter
let add = document.getElementById("increment1"); //from the increment 1 button (green arrow)
let subtract = document.getElementById("decrement1"); //from the decrement 1 button (red arrow)

let int = document.getElementById("number"); // number for the section that takes care of increment 1, decrement 1
let integer = 0;

add.addEventListener("click", function(){ // When the green arrow is clicked the integer variable increments if it's within the range -20 ~ 19
    if(integer < 20 && integer >= -20){
        integer += 1;
    }
    int.innerHTML = integer;
})

subtract.addEventListener("click", function(){ // When the red arrow is clicked the integer variable decrements if it's within the range -19 ~ 20
    if(integer <= 20 && integer > -20){
        integer -= 1;
    }
    int.innerHTML = integer;
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
        window.location.href = "/start";
    }
})

















function sendGetRequest(variable, value) {
  const data = { variableName: variable, value: value };
  const url = 'http://192.168.1.100/data';

  fetch(`${url}?${new URLSearchParams(data)}`, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      console.log(`GET request sent successfully for ${variable} = ${value}`);
    })
    .catch(error => {
      console.error(`Error sending GET request for ${variable} = ${value}:`, error);
    });
}






