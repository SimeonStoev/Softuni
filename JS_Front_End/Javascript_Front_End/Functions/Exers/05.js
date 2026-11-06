function checkPalindromeInArrayElems(arr) {

    function isPalindrome(number) {
        let numberStr = number.toString();
        for (let i = 0; i < numberStr.length / 2; i++) {
            if (numberStr[i] !== numberStr[numberStr.length - 1 - i]) {
                return false;
            }
        }
        return true;
    }

    for (let number of arr) {
        if (isPalindrome(number)) {
            console.log("true");
        } else {
            console.log("false");
        }
    }

}

checkPalindromeInArrayElems([32, 2, 232, 1010]);