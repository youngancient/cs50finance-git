const errorsize = document.querySelector(".error-size");
const errornone = document.querySelector(".error-none");
document.addEventListener("DOMContentLoaded", function(){
    const form = document.querySelector('form');
    const image = document.querySelector("#image");
    image.onchange = function(){
        document.querySelectorAll(".error").forEach(error=>{
            error.classList.remove('show');
        })
        validateSize(image);
    };
    form.addEventListener('submit', (e)=>{
        let imageCont = image.files[0];
        if(imageCont == undefined){
            errornone.classList.add('show');
            e.preventDefault();
        }else{
            if(validateSize(image)==false){
                e.preventDefault();
            }
        }
    })
});

function validateSize(input) {
    const fileSize = input.files[0].size / 1024 / 1024; // in MiB
    if (fileSize > 2) {
        errorsize.innerHTML = 'File size exceeds 2 MiB, Reupload!';
        errorsize.classList.add('show');
        return false;
    }else{
        errorsize.classList.remove('error');
        errorsize.classList.add('success');
        errorsize.innerHTML = 'File size is less than 2 MiB';
        errorsize.classList.add('show');
    }
  }