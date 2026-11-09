function radioCrystals(list) {
    const target = list[0];

    let operationsList = [
        "Cut",
        "Lap",
        "Grind",
        "Etch",
    ]

    let operations = {
        "Cut": (a) => a / 4,
        "Lap": (a) => a * 0.8,
        "Grind": (a) => a - 20,
        "Etch": (a) => a - 2,
        "XRay": (a) => a + 1,
        "TrasportAndWash": (a) => Math.floor(a)
    };

    for (let i = 1; i < list.length; i++) {
        let currChunk = list[i];

        if (currChunk <= target) {
            if (currChunk === target - 1) {
                console.log(`Processing chunk ${currChunk} microns`);
                currChunk++;
                console.log("X-ray x1");
                console.log(`Finished crystal ${currChunk} microns`);
            }
            continue;
        }

        console.log(`Processing chunk ${currChunk} microns`);

        for (let j = 0; j < operationsList.length; j++) {
            let operation = operationsList[j];
            let operationCount = 0;

            while (operations[operation](currChunk) >= target) {
                currChunk = operations[operation](currChunk);
                operationCount++;
            }

            if (Math.floor(operations[operation](currChunk)) === target - 1) {
                currChunk = target;
                operationCount++;

                console.log(`${operation} x${operationCount}`)
                console.log("Transporting and washing");
                console.log("X-ray x1");
                break;
            }

            if (operationCount > 0) {
                console.log(`${operation} x${operationCount}`)
                currChunk = operations["TrasportAndWash"](currChunk);
                console.log("Transporting and washing");
            }
        }

        console.log(`Finished crystal ${currChunk} microns`);
    }
}

radioCrystals([100, 99]);