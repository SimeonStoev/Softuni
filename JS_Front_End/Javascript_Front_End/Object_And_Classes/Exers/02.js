function solve(townList) {
    class Town {
        constructor(town, latitude, longitude) {
            this.town = town;
            this.latitude = latitude;
            this.longitude = longitude;
        }

        print() {
            console.log({ ...this });
        }
    }

    let towns = [];

    for (let townData of townList) {
        let [town, latitude, longitude] = townData.split(" | ");
        towns.push(new Town(town, Number(latitude).toFixed(2), Number(longitude).toFixed(2)));
    }

    for (let town of towns) {
        town.print();
    }
}

solve(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']
);