function handleVKeyboard()
{
element = document.getElementById("vkeyboard");

if(element.classList.contains("hide"))
{
    element.classList.remove("hide");
    element.classList.add("show");
    element = document.getElementById("vkeyboard_icon");
    element.classList.add("fas");
    element.classList.remove("far");
}
else
{
element.classList.remove("show");
element.classList.add("hide");
element = document.getElementById("vkeyboard_icon");
element.classList.add("far");
element.classList.remove("fas");
}
}

let Keyboard = window.SimpleKeyboard.default;

let myKeyboard = new Keyboard({
  onChange: input => onChange(input),
  onKeyPress: button => onKeyPress(button)
});

function onChange(input) {
  document.querySelector(".virtual-keyboard").value = input;
}


function onKeyPress(button) {
  //console.log("Button pressed", button);
}


