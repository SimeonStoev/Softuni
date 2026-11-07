function subtract(num1, num2, num3) {

    function sum(numOne, numTwo) {
        return numOne + numTwo;
    }

    function doSubtract(sumTwoNums, numThree) {
        return sumTwoNums - numThree;
    }

    console.log(doSubtract(sum(num1, num2), num3))

}

subtract(23, 6, 10);