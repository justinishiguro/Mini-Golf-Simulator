

// if(window.location.pathname == "http://127.0.0.1:5500/webapp/gamePage.html"){

console.log(window.location.pathname);

// }

document.addEventListener("keydown", function(event){
    if(event.key == 's'){
        window.location.href = "http://127.0.0.1:5500/webapp/GAME_PAGE/gamePage.html"
    }
    console.log(event.key);
})

