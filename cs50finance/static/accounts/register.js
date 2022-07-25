document.addEventListener("DOMContentLoaded", function(){
    const form = document.querySelector("form");
    const username = document.querySelector('#username');
    const password = document.querySelector('#password');
    const password2 = document.querySelector('#password2');
    const errorName = document.querySelector('.error-name');
    const errorPassword = document.querySelectorAll('.error-password');
    username.onkeyup = function(){
        errorName.classList.remove('show')
    }
    password.onkeyup = function(){
        errorPassword.forEach(error =>{
            error.classList.remove('show')
        })
    }
    password2.onkeyup = function(){
        errorPassword.forEach(error =>{
            error.classList.remove('show')
        })
    }
    form.addEventListener('submit', (e)=>{
        if(username.value == '' && password.value == ''){
            e.preventDefault();
            errorName.classList.add('show')
            errorPassword.forEach(error =>{
                error.innerHTML = "Password cannot be empty";
                error.classList.add('show')
            })
        }else if(username.value == ""){
            e.preventDefault();
            errorName.classList.add('show')
        }else if(password.value == ''){
            e.preventDefault();
            errorPassword.forEach(error =>{
                error.innerHTML = "Password cannot be empty";
                error.classList.add('show')
            })
        }else if(password.value.length < 8){
            e.preventDefault();
            errorPassword.forEach(error =>{
                error.innerHTML = `${password.value.length}chars Too weak: Min is 8chars`;
                error.classList.add('show')
            })
        }else if(password.value !== password2.value){
            e.preventDefault();
            errorPassword.forEach(error =>{
                error.innerHTML = "Passwords do not match";
                error.classList.add('show')
            })
        }else{
            document.querySelectorAll('.error').forEach(error =>{
                error.classList.remove('show');
            })
        }
    })
})
