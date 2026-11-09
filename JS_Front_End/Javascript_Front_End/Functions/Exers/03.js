function printCharsBetweenTwoAsciiSymbols(charOne, charTwo) {
    let smallerAsciiCode = Math.min(charOne.charCodeAt(), charTwo.charCodeAt());
    let biggerAsciiCode = Math.max(charOne.charCodeAt(), charTwo.charCodeAt());
    let result = "";

    for (let i = smallerAsciiCode + 1; i < biggerAsciiCode; i++) {
        result += String.fromCharCode(i) + " ";
    }

    console.log(result.trim());
}

printCharsBetweenTwoAsciiSymbols('C',
    '#'
);