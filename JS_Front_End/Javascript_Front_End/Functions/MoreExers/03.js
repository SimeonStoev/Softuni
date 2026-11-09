function pointValidation(pointList) {

    function isValidDistanceBetPoints(a1, a2, b1, b2) {
        let distance = Math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2);
        return Number.isInteger(distance);
    }

    let x1 = pointList[0], y1 = pointList[1], x2 = pointList[2], y2 = pointList[3];

    if (isValidDistanceBetPoints(x1, y1, 0, 0)) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }

    if (isValidDistanceBetPoints(x2, y2, 0, 0)) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    } else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }

    if (isValidDistanceBetPoints(x1, y1, x2, y2)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}

pointValidation([2, 1, 1, 1]);