
function generate() {
    let dictionary = "";
    if (document.getElementById("lowercase").checked) {
        dictionary += "qwertyuiopasdfghjklzxcvbnm";
    }
    if (document.getElementById("uppercase").checked) {
        dictionary += "QWERTYUIOPASDFGHJKLZXCVBNM";
    }
    if (document.getElementById("number").checked) {
        dictionary += "1234567890";
    }
    if (document.getElementById("symbol").checked) {
        dictionary += "!@#$%^&*()_+-={}[];<>:";
    }

    const length = document.querySelector('.slider').value;


    if (length < 1 || dictionary.length === 0) {
        return;
    }
    let password = "";
    for (let i = 0; i < length; i++) {
        const pos = Math.floor(Math.random() * dictionary.length);
        password += dictionary[pos]; 
    }
    document.querySelector('.display').value = password;
}
document.querySelector('.slider').addEventListener("input",(e) => {
    document.querySelector("div.lengthh span").innerHTML = e.target.value;
    generate()
})
document.querySelectorAll('.option input[type="checkbox"], button.generatebutton')
  .forEach((elem) => {
      elem.addEventListener("click", generate);
  });
document.querySelector(".copy").addEventListener("click", () => {
  const password = document.querySelector(".display").value;
  if (password) {
    navigator.clipboard.writeText(password);
    alert("Password copied to clipboard!");
  }
});
