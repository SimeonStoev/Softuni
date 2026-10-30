function calcArmourRepair(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let repairSum = 0;
    shieldBreaks = 0;

    for (let fight = 1; fight <= lostFights; fight++) {
        if (fight % 2 === 0) {
            repairSum += helmetPrice;
        }
        if (fight % 3 === 0) {
            repairSum += swordPrice;
        }

        if (fight % 2 === 0 && fight % 3 === 0) {
            repairSum += shieldPrice;
            shieldBreaks++;
            if (shieldBreaks % 2 === 0) {
                repairSum += armorPrice;
            }

        }
    }

    console.log(`Gladiator expenses: ${repairSum.toFixed(2)} aureus`);
}

calcArmourRepair(23, 12.50, 21.50, 40, 200);