const display = document.getElementById("display")
function clearDisplay(){
    display.value ="";

}
function appendoperation(input){
    display.value += input
   
}
function appendnumber(input){
    display.value += input

}
function calculate() {
  try {
    display.value = eval(display.value);
  } catch (error) {
    display.value = "Error";
  }
}