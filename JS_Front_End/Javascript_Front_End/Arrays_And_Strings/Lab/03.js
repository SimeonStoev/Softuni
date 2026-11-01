function evenAndOddSubstr(list) {
    evenSum = list.reduce((acc, curr) => acc + (curr % 2 == 0 ? curr : 0), 0);
    oddSum = list.reduce((acc, curr) => acc + (curr % 2 != 0 ? curr : 0), 0);
    console.log(evenSum - oddSum);
}

evenAndOddSubstr([2, 4, 6, 8, 10]);