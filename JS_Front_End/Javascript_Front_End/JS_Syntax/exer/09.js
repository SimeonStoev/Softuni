function calcMoneyForFruits(fruit, weight, pricePerKg) {
    let weightKg = weight / 1000;
    let totalPrice = weightKg * pricePerKg;
    console.log(`I need $${totalPrice.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruit}.`);
}

calcMoneyForFruits('orange', 2500, 1.80);
calcMoneyForFruits('apple', 1563, 2.35);
calcMoneyForFruits('banana', 2000, 1.50);