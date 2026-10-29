function calcDistance(x1, y1, x2, y2) {
    // (x1, y1) -> (0, 0)
    let length1 = Math.sqrt(x1 ** 2 + y1 ** 2);
    // (x2, y2) -> (0, 0)
    let length2 = Math.sqrt(x2 ** 2 + y2 ** 2);
    // distance between (x1, y1) and (x2, y2)
    let distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);

    if (Number.isInteger(length1)) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    }
    else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }
    if (Number.isInteger(length2)) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    }
    else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }
    if (Number.isInteger(distance)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    }
    else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}

calcDistance(2, 1, 1, 1);