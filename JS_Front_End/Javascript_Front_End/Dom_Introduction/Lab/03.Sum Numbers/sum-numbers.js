function calc() {
    // TODO
    let sum = 0;
    let firstEl = document.getElementById("num1");
    let secondEl = document.getElementById("num2");
    let sumEl = document.getElementById("sum");
    sum = Number(firstEl.value) + Number(secondEl.value);
    sumEl.value = sum;
}