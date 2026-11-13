function solve(garagesData) {
    class Garage {
        constructor(number, car) {
            this.number = number;
            this.cars = [car];
        }

        addCar(car) {
            this.cars.push(car);
        }

        print() {
            console.log(`Garage № ${this.number}`);
            for (let carData of this.cars) {
                let result = [];

                for (let carDescr of carData.split(", ")) {
                    let [key, value] = carDescr.split(": ");
                    result.push(`${key} - ${value}`);
                }
                console.log(`--- ${result.join(", ")}`)
            }
        }
    }

    function getGarageIndex(garageNumber, garagesList) {
        for (let i = 0; i < garagesList.length; i++) {
            if (garageNumber === garagesList[i].number) {
                return i;
            }
        }
        return -1;
    }

    let garages = [];
    for (let garage of garagesData) {
        let [garageNumber, car] = garage.split(" - ");
        let garageIndex = getGarageIndex(garageNumber, garages);
        if (garageIndex === -1) {
            garages.push(new Garage(garageNumber, car));
        } else {
            garages[garageIndex].addCar(car);
        }
    }

    for (let garage of garages) {
        garage.print();
    }
}

solve(['1 - color: green, fuel type: petrol',
    '1 - color: dark red, manufacture: WV',
    '2 - fuel type: diesel',
    '3 - color: dark blue, fuel type: petrol']
);