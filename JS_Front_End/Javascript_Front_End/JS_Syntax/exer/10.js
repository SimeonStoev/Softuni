function isNNumberWithSameDigits(num) {
    let isSame = true;
    let sum = 0;
    let numbToString = num.toString();
    for (let digit of numbToString) {
        if (digit !== numbToString[0]) {
            isSame = false;
        }
        sum += Number(digit);
    }
    console.log(isSame);
    console.log(sum);
}

isNNumberWithSameDigits(2222222); // true, 14
isNNumberWithSameDigits(1234); // false, 10