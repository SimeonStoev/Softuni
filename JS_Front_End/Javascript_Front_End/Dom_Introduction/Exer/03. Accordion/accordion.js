function toggle() {
    //TODO
    let button = document.getElementsByClassName('button')[0];
    let divEl = document.getElementById("extra");
    if (button.textContent === "More") {
        divEl.style.display = "block";
        button.textContent = "Less";
    } else {
        divEl.style.display = "none";
        button.textContent = "More";
    }
}