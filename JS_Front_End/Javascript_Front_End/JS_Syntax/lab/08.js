function solve(argument) {
    let argType = typeof argument;
    if (argType === "number") {
        let circleArea = Math.PI * argument ** 2;
        console.log(circleArea.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${argType}.`);
    }
}

solve(42); // Output: "number"
solve("Hello"); // Output: "string"
solve(true); // Output: "boolean"
solve({}); // Output: "object"
solve(null); // Output: "object"
solve(undefined); // Output: "undefined"
solve(20.1); // Output: "number"