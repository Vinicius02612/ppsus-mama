

send = document.getElementsByClassName(".send")
send.addEventListener("click", validateLogin)

function validateLogin(e){
    let  user = document.getElementById("#usuario")
    let password = document.getElementById("#senha")
    let validaUser = document.getElementById("validaUser")
    let validaPassWord = document.getElementById("validaPassWord")

    let valid = true
    e.preventDefault()
    
    if(user.value == "" && password == ""){
        validaUser.classList.add("visible")
    }
}