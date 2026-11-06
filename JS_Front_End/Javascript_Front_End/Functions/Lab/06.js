function signCheck(numOne, numTwo, numThree) {
    let signList = [numOne < 0 ? "N" : "P", numTwo < 0 ? "N" : "P", numThree < 0 ? "N" : "P"];
    let negativesCount = 0;
    for (let elem of signList) {
        if (elem === "N") {
            negativesCount++;
        }
    }

    if (negativesCount === 1 || negativesCount === 3) {
        console.log("Negative");
    } else {
        console.log("Positive")
    }
}

signCheck(-5,
    1,
    1
);