function solve(num1, num2, operator) {
    switch (operator) {
        case "+":
            console.log(num1 + num2);
            break;
        case "-":
            console.log(num1 - num2);
            break;
        case "*":
            console.log(num1 * num2);
            break;
        case "/":
            console.log(num1 / num2);
            break;
        case "%":
            console.log(num1 % num2);
            break;
        case "**":
            console.log(num1 ** num2);
            break;
        default:
            console.log("Error!");
    }
}


solve(5, 6, "+");
solve(5, 6, "-");
solve(5, 6, "*");
solve(5, 6, "/");
solve(5, 6, "%");
solve(5, 6, "**");