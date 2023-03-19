

// if(window.location.pathname == "http://127.0.0.1:5500/webapp/gamePage.html"){

console.log(window.location.pathname);

// }

document.addEventListener("keydown", function(event){
    if(event.key == 's'){
        window.location.href = "/game"
    }
    console.log(event.key);
})

