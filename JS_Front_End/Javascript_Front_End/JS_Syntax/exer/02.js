function calcPriceForVacation(numberOfPeople, groupType, day) {
    let price = 0;

    if (groupType === "Students") {
        if (day === "Friday") {
            price = numberOfPeople * 8.45;
        } else if (day === "Saturday") {
            price = numberOfPeople * 9.80;
        } else if (day === "Sunday") {
            price = numberOfPeople * 10.46;
        }
    } else if (groupType === "Business") {
        if (numberOfPeople >= 100) {
            numberOfPeople -= 10;
        }
        if (day === "Friday") {
            price = numberOfPeople * 10.90;
        } else if (day === "Saturday") {
            price = numberOfPeople * 15.60;
        } else if (day === "Sunday") {
            price = numberOfPeople * 16;
        }
    } else if (groupType === "Regular") {
        if (day === "Friday") {
            price = numberOfPeople * 15.00;
        } else if (day === "Saturday") {
            price = numberOfPeople * 20;
        } else if (day === "Sunday") {
            price = numberOfPeople * 22.50;
        }
    }

    if (groupType === "Students" && numberOfPeople >= 30) {
        price *= 0.85;
    } else if (groupType === "Regular" && numberOfPeople >= 10 && numberOfPeople <= 20) {
        price *= 0.95;
    }

    console.log(`Total price: ${price.toFixed(2)}`);
}

calcPriceForVacation(30, "Students", "Sunday");
calcPriceForVacation(40, "Regular", "Saturday");
calcPriceForVacation(110, "Business", "Friday");