function calculatorOperation(numOne, numTwo, operator) {

    const operations = {
        'add': (a, b) => a + b,
        'subtract': (a, b) => a - b,
        'multiply': (a, b) => a * b,
        'divide': (a, b) => a / b
    };

    console.log(operations[operator](numOne, numTwo));
}

calculatorOperation(50,
    13,
    'subtract'
);