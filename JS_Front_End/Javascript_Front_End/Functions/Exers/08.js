function checkIfNumberIsPerfect(number) {
    if (!Number.isInteger(number) || number < 1) {
        console.log("It's not so perfect.");
        return;
    }
    let numberDivisors = [];
    for (let digit = 1; digit < number; digit++) {
        if (number % digit === 0) {
            numberDivisors.push(digit);
        }
    }

    let sum = numberDivisors.reduce((totalSum, elem) => totalSum + elem, 0);

    if (sum === number) {
        console.log("We have a perfect number!")
    } else {
        console.log("It's not so perfect.");
    }


}

checkIfNumberIsPerfect(1236498);