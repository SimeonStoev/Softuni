function solve(list) {
    let parkingLot = [];

    for (let i = 0; i < list.length; i++) {
        let [direction, carNumber] = list[i].split(", ");

        let carIndex = parkingLot.indexOf(carNumber);

        if (direction === "IN" && carIndex === -1) {
            parkingLot.push(carNumber);
        } else if (direction === "OUT") {
            if (carIndex !== -1) {
                parkingLot.splice(carIndex, 1);
            }
        }
    }

    if (parkingLot.length === 0) {
        console.log("Parking Lot is Empty");
    } else {
        for (let carNumber of parkingLot.sort((a, b) => a.localeCompare(b))) {
            console.log(carNumber)
        }
    }
}

solve(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA']
);