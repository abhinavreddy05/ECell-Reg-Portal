const fields = document.getElementsByClassName('input-group')
const btns = document.getElementsByClassName('nav-button')

var page = 1;

function disable(a, b){
    for (let i = a; i < b; i++) {
        fields[i].style.display = "none"    
    }
}

function enable(a, b) { 
    for (let i = a; i < b; i++) {
        fields[i].style.display = "block"    
    }
}

btns[1].addEventListener('click', ()=>{
    if (page == 1) {
        page = 2
        disable(0, 6)
        enable(6, 12)
        btns[0].disabled = false
        btns[1].style.display = "none"
        btns[2].style.display = "block"
    }
})

btns[0].addEventListener('click', ()=>{
    if (page == 2) {
        page = 1;
        enable(0, 6)
        disable(6, 12)
        btns[0].disabled = true
        btns[1].disabled = false
        btns[1].style.display = "block"
        btns[2].style.display = "none"
    }
})

disable(6, 12)