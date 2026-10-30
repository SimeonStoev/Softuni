function printAndSum(a, b) {
    let sum = 0;
    let result = "";
    for (let i = a; i <= b; i++) {
        sum += i;
        result += i + " ";
    }
    console.log(result.trim());
    console.log("Sum: " + sum);
}

printAndSum(5, 10);
printAndSum(0, 26);
printAndSum(50, 60);