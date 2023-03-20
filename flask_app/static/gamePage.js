//Slider
var bar = document.getElementById("myRange");
var valueOutput = document.getElementById("value");

valueOutput.innerHTML = bar.ariaValueMax;
bar.oninput = function() {
    valueOutput.innerHTML = this.value;
}

setInterval(() => {
    console.log("sent a request and ardi has a small pp")
}, 5000)

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
let add2 = document.getElementById("increment2"); //from the increment 1 button (blue arrow)
let subtract2 = document.getElementById("decrement2"); //from the decrement 1 button (yellow arrow)

let int2 = document.getElementById("number2"); // number for the section that takes care of increment 2, decrement 2
let integer2 = 0;



add2.addEventListener("click", function(){ // When the blue arrow is clicked the integer variable increments if it's within the range -20 ~ 19
    if(integer2 < 20 && integer2 >= -20){
        integer2 += 1;
    }
    int2.innerHTML = integer2;
    // console.log(integer2);
})

subtract2.addEventListener("click", function(){ // When the yellow arrow is clicked the integer variable decrements if it's within the range -19 ~ 20
    if(integer2 <= 20 && integer2 > -20){
    integer2 -= 1;
    }
    int2.innerHTML = integer2;
    // console.log(integer2);
})


let which_key = "NULL";
document.addEventListener("keydown", function(event) { 
    which_key = event.key;
    if(which_key == "ArrowLeft"){ // basically does the same functionality as the yellow arrow but with the 'left' direcetion key
        if(integer2 <= 20 && integer2 > -20){
            integer2 -= 1;
            }
        int2.innerHTML = integer2;
    }

    else if(which_key == "ArrowDown"){ // basically does the same functionality as the red arrow but with the 'down' direction key
        if(integer <= 20 && integer > -20){
            integer -= 1;
        }
        int.innerHTML = integer;
    }

    else if(which_key == "ArrowUp"){ // basically does the same functionality as the green arrow but with the 'up' direction key
        if(integer < 20 && integer >= -20){
            integer += 1;
        }
        int.innerHTML = integer;
    }

    else if(which_key == "ArrowRight"){ // basically does the same functionality as the blue arrow but with the 'right' direction key
        if(integer2 < 20 && integer2 >= -20){
            integer2 += 1;
        }
        int2.innerHTML = integer2;
    }
    else if(which_key == "r"){ // it resets the values to '0' when the 'r' key is pressed
        integer = 0;
        integer2 = 0;
        int.innerHTML = 0;
        int2.innerHTML = 0;
    }
    else;
});


document.addEventListener("keydown", function(event) { // 
    if(event.key == "ArrowUp" || event.key == "ArrowDown" || event.key == "ArrowLeft" || event.key == "ArrowRight"){
        event.preventDefault();
    }
})

document.addEventListener("keydown", function(event){ // if the keyboard button 'q' is presed it directs the user to the start page
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







