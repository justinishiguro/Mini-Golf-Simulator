

document.addEventListener("keydown", function(event){
    if(event.key == 's'){
        window.location.href = "/game"
    }
    console.log(event.key);
})

// when the keyboard key 's' is pressed it directs the user from the game page to the start page