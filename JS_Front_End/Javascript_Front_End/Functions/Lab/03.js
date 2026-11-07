function repeatStringNTimes(str, n) {
    let newString = "";
    for (let i = 1; i <= n; i++) {
        newString += str;
    }
    return newString;
}

console.log(repeatStringNTimes("String", 2));