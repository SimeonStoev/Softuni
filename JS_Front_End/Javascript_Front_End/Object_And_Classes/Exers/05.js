function solve(heroesDataList) {
    class Hero {
        constructor(name, level, items) {
            this.name = name;
            this.level = level;
            this.items = items;
        }

        print() {
            console.log(`Hero: ${this.name}`);
            console.log(`level => ${this.level}`);
            if (this.items !== "") {
                console.log(`items => ${this.items}`);
            }
        }
    }

    let heroes = [];

    for (let heroData of heroesDataList) {
        let heroList = heroData.split(" / ");
        let name = heroList[0];
        let level = Number(heroList[1]);
        let items = (heroList.length === 3) ? heroList[2] : "";
        heroes.push(new Hero(name, level, items));
    }

    for (let hero of heroes.sort((a, b) => a.level - b.level)) {
        hero.print();
    }
}

solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
]
);