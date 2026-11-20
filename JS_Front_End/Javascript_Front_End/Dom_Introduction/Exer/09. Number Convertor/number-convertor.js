function solve() {
    // TODO
    function convertDecimalToBinary(number) {
        let result = [];
        while (number !== 0) {
            if (number === 1) {
                result.push(1);
                break;
            }
            result.push(number % 2);
            number = Math.floor(number / 2);
        }
        return result.reverse().join("");
    }

    function convertDecimalToHex(number) {
        let result = [];
        const hexDict = {
            0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
            10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
        };

        while (number !== 0) {
            result.push(hexDict[number % 16]);
            number = Math.floor(number / 16);
        }

        return result.reverse().join("");
    }

    const decimalInput = document.getElementById('input').value;
    const convertionType = document.getElementById("selectMenuTo").value;
    let convertValue = "";

    if (convertionType === "binary") {
        convertValue = convertDecimalToBinary(decimalInput);
    } else if (convertionType === "hexadecimal") {
        convertValue = convertDecimalToHex(decimalInput);
    }

    let result = document.getElementById("result");
    result.value = convertValue;
}