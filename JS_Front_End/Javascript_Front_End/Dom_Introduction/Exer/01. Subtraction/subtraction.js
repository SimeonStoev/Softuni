function subtract() {
    //TODO
    const firstNumberElVal = Number(document.querySelector("#firstNumber").value);
    const secondNumberElVal = Number(document.getElementById("secondNumber").value);
    let result = document.getElementById("result");
    result.textContent = firstNumberElVal - secondNumberElVal;
}