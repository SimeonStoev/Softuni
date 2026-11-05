function consumeSpiciesFromYield(currentYield) {
    let days = 0;
    const dailyConsumption = 26;
    let consumedSpices = 0;

    while (currentYield >= 100) {
        days++;
        consumedSpices += currentYield - dailyConsumption;
        currentYield -= 10;
    }

    if (consumedSpices - dailyConsumption <= 0) {
        consumedSpices = 0;
    } else {
        consumedSpices -= dailyConsumption;
    }

    console.log(days);
    console.log(consumedSpices);
}

consumeSpiciesFromYield(450);