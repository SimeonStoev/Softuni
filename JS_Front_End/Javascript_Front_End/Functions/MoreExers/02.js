function numberModification(number) {

    function getAverage(numb) {
        let numbStr = numb.toString();
        let sum = 0;
        for (let i = 0; i < numbStr.length; i++) {
            sum += Number(numbStr[i]);
        }

        return sum / numbStr.length;
    }

    let flag = true;

    while (flag) {
        if (getAverage(number) >= 5) {
            flag = false;
        } else {
            number = number * 10 + 9;
        }
    }

    console.log(number);
}

numberModification(5835);