function carWash(commands) {
    let value = 0;
    for (let command of commands) {
        if (command === "soap") {
            value += 10;
        } else if (command === "water") {
            value += value * 0.2;
        } else if (command === "vacuum cleaner") {
            value += value * 0.25;
        } else if (command == "mud") {
            value -= value * 0.1;
        }
    }

    console.log(`The car is ${value.toFixed(2)}% clean.`)
}

carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]);