document.addEventListener("DOMContentLoaded", function(){
    const icon = document.querySelector(".icon");
    const dropDown = document.querySelector(".mobile-drop-down");
    isClicked = false;
    icon.onclick = ()=>{
        icon.classList.toggle("fa-xmark");
        if(!isClicked){
            dropDown.style.display = "flex";
            isClicked = true;
        } else{
            dropDown.style.display = "none";
            isClicked = false;

        }
    }
});