//Slider
var bar = document.getElementById("myRange");
var valueOutput = document.getElementById("value");

valueOutput.innerHTML = bar.ariaValueMax;
bar.oninput = function() {
	valueOutput.innerHTML = this.value;
}

let hit_button = document.getElementsByClassName("hitButton")[0];
hit_button.addEventListener("click", function(event){
	console.log("True");
    makeRequests("Hit" , "True");
   // makeRequests("Hit-value", valueOutput.innerHTML);
});


let hit_value;

bar.addEventListener("input", function(){

	hit_value = valueOutput.innerHTML;
	makeRequests("Hit-value", hit_value);
});

// setInterval(() => {
//     fetch("http://localhost:3000")
//             .then((res) => {
// 	        return res.json()
// 		})
// 		.then((res2) => console.log(res2))
// }, 500)

function makeRequests(variable, value){

    fetch('http://localhost:3000', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: createJsonString(variable, value)
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => console.log('POST response:' ,data))
        .catch((error) => console.error('ERROR', error));
}

var yo = false;


// async function fetchData() {
//     const res = await fetch('/hole', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({key: 'value'})
//     });
//     const t = await res.json();
//     console.log(t.data); // print the 'data' value in the response to the console
//     return JSON.stringify(t);
// }

async function fetchData() {
    const payload = {key: 'value'};
    console.log('Sending payload:', payload);
    const res = await fetch('/hole1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
    const t = await res.json();
    console.log('Received data:',JSON.stringify(t));
    return JSON.stringify(t);
}

// function fetchData(){
//     $.ajax({
//         url: "'/hole1",
//         type: "POST",
//         success: function(data){

//         }
//     });


// }


// async function fetchData() {
//     const res = await fetch('/hole', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     });
//     const data = await res.json();
//     console.log('Received data:', data.data);
//     return JSON.stringify(data);
// }


function createJsonString(varname, value){
    const jsonObj = {
        [varname] : value
    };

    const jsonString = JSON.stringify(jsonObj);
    return jsonString
}

//Counter
let add = document.getElementById("increment1"); //from the increment 1 button (green arrow)
let subtract = document.getElementById("decrement1"); //from the decrement 1 button (red arrow)

let height = document.getElementById("number"); // number for the section that takes care of increment 1, decrement 1
let integer = 0;

add.addEventListener("click", function(){ // When the green arrow is clicked the integer variable increments if it's within the range -20 ~ 19
    if(integer < 45 && integer >= 0){
        integer += 1;
    }
    height.innerHTML = integer;
    makeRequests("Height", integer);

})

subtract.addEventListener("click", function(){ // When the red arrow is clicked the integer variable decrements if it's within the range -19 ~ 20
    if(integer <= 45 && integer > 0){
        integer -= 1;
    }
    height.innerHTML = integer;
    makeRequests("Height", integer);


})

//Counter2
let add2 = document.getElementById("increment2"); //from the increment 1 button (blue arrow)
let subtract2 = document.getElementById("decrement2"); //from the decrement 1 button (yellow arrow)

let rotation = document.getElementById("number2"); // number for the section that takes care of increment 2, decrement 2
let integer2 = 0;





add2.addEventListener("click", function(){ // When the blue arrow is clicked the integer variable increments if it's within the range -20 ~ 19
    rotation.textContent = "Right";
    makeRequests("Rotation", "Right")
})

subtract2.addEventListener("click", function(){ // When the yellow arrow is clicked the integer variable decrements if it's within the range -19 ~ 20

    rotation.textContent = yo.toString();


    makeRequests("Rotation","Left");
})

//Reach buttons

let fw = document.getElementById("forward");
let bw = document.getElementById("backward");

let int3 = document.getElementById("number3");
let integer3 = 0;

fw.addEventListener("click", function(){
    if(integer3 < 50 && integer3 >= 0){
        integer3 += 5;
    }

    // if(integer3 == 20){
    //     var ball1_var = document.getElementById("ball1");
    //     ball1_var.style.backgroundImage = "url('../static/images/GreenBall.png')";
    // }
    int3.innerHTML = integer3;
    makeRequests("Reach" ,integer3);
})

bw.addEventListener("click", function(){
    if(integer3 <= 50 && integer3 > 0){
        integer3 -= 5;
    }
    int3.innerHTML = integer3;
    makeRequests("Reach", integer3);
})

let which_key = "NULL";
document.addEventListener("keydown", function(event) {
    which_key = event.key;
    if(which_key == "ArrowLeft"){ // basically does the same functionality as the yellow arrow but with the 'left' direcetion key
        rotation.textContent = fetchData();
        makeRequests("Rotation", "Left")
    }

    else if(which_key == "ArrowDown"){ // basically does the same functionality as the red arrow but with the 'down' direction key
        if(integer <= 45 && integer > 0){
            integer -= 1;
        }
        height.innerHTML = integer;
        makeRequests("Height", integer);

    }

    else if(which_key == "ArrowUp"){ // basically does the same functionality as the green arrow but with the 'up' direction key
        if(integer < 45 && integer >= 0){
            integer += 1;
        }
        height.innerHTML = integer;
        makeRequests("Height", integer);

    }

    else if(which_key == "ArrowRight"){ // basically does the same functionality as the blue arrow but with the 'right' direction key
        rotation.textContent = "Right";
        makeRequests("Rotation", "Right");

    }
    else if(which_key == "r"){ // it resets the values to '0' when the 'r' key is pressed
        integer = 0;
        integer2 = 0;
        height.innerHTML = 0;
        rotation.innerHTML = 0;

        makeRequests("Hit-value", valueOutput.innerHTML);
        makeRequests("Height", integer);

    }
    else if(which_key == "w"){
        if(integer3 < 50 && integer3 >= 0){
            integer3 += 5;
        }

        int3.innerHTML = integer3;
        makeRequests("Reach" ,integer3);
    }
    else if(which_key == "s"){
        if(integer3 <= 50 && integer3 > 0){
            integer3 -= 5;
        }
        int3.innerHTML = integer3;
        makeRequests("Reach", integer3);

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

document.addEventListener("keydown", function(event){
    if(event.key == "Enter"){
        startTimer();
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


function sendPostRequest(variable, value) {
    const data = { variableName: variable, value: value };
    const url = 'http://localhost:3000';

    fetch(`${url}?${new URLSearchParams(data)}`, {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body : JSON.stringify(data)
    })
        .then(response => {
            console.log(`POST request sent successfully for ${variable} = ${value}`);
        })
        .catch(error => {
            console.error(`Error sending POST request for ${variable} = ${value}:`, error);
        });
}

let timer = document.getElementById("timer");
let progressBar = document.getElementsByClassName("progress2")[0];
let progress_ = document.getElementsByClassName("progress-bar")[0];

let remaining_time = 90;

const progressWidth = ((remaining_time) / 90) * 100;
progress_.style.width = `${progressWidth}%`;

function startTimer(){
    const intervalId = setInterval (() => {
        remaining_time -= 1;

        const min = Math.floor((remaining_time % 3600)/60);
        const sec = remaining_time % 60;

        const formattedTime = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
        timer.textContent = formattedTime;

        const progressWidth = (remaining_time/ 90) * 100;
        progress_.style.width =  `${progressWidth}%`;

        if(remaining_time <= 30){
            progressBar.style.backgroundColor = "red";
            progressBar.style.opacity = 0.5;
            progress_.style.width = `${(remaining_time / 90) * 100}%`;
        }
        else if (remaining_time <= 60) {
            progressBar.style.backgroundColor = "orange";
            progressBar.style.opacity = 0.5;
            progress_.style.width = `${(remaining_time / 90) * 100}%`;
        }

        if(remaining_time <= 0){

            window.location.href = "/end";
        }
    },1000);
}

// export let ball1 = false;
// export let ball2 = false;
// export let ball3 = false;
// export let ball4 = false;
// export let ball5 = false;
// export let ball6 = false;
