function factorialDivisionOfTwoNumbers(numbOne, numbTwo) {

    function factorial(n) {
        if (n === 1 || n === 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    console.log((factorial(numbOne) / factorial(numbTwo)).toFixed(2));
}

factorialDivisionOfTwoNumbers(6, 2);