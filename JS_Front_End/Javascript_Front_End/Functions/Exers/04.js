function printEvenAndOddSumOfNumber(number) {
    let evenSum = 0;
    let oddSum = 0;
    let numberCopy = number;
    let digit = 0;

    while (numberCopy > 0) {
        digit = numberCopy % 10;
        if (digit % 2 === 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }

        numberCopy = Math.trunc(numberCopy / 10);
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

printEvenAndOddSumOfNumber(3495892137259234);