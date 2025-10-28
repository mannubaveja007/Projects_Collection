const togglebutton = document.getElementById('theme-toggle')
const body = document.body
body.classList.add('light-mode')
togglebutton.addEventListener("click",()=>{
    if(body.classList.contains('light-mode')){
        body.classList.replace('light-mode','dark-mode');
        togglebutton.textContent = "switch to light mode"
    }
    else{
        body.classList.replace('dark-mode', 'light-mode');
        togglebutton.textContent = 'Switch to Dark Mode';
    }
})