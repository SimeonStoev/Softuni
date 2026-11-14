function solve(commands) {
    class Army {
        constructor(name, count) {
            this.name = name;
            this.count = count;
        }

        printInfo() {
            console.log(`>>> ${this.name} - ${this.count}`);
        }
    }

    class Leader {
        constructor(name, army) {
            this.name = name;
            this.armies = army !== "" ? [army] : [];
            this.totalArmiesCount = army !== "" ? army.count : 0;
        }

        addArmy(army) {
            this.armies.push(army);
            this.totalArmiesCount += army.count;
        }

        printInfo() {
            console.log(`${this.name}: ${this.totalArmiesCount}`);
            for (let army of this.armies.sort((a, b) => b.count - a.count)) {
                army.printInfo();
            }
        }
    }

    function getLeaderIndex(leaderName, leaders) {
        for (let i = 0; i < leaders.length; i++) {
            if (leaders[i].name === leaderName) {
                return i;
            }
        }
        return -1;
    }

    function addCountToArmyIfExists(armyName, count, leaders) {
        for (let leader of leaders) {
            for (let army of leader.armies) {
                if (army.name === armyName) {
                    army.count += count;
                    leader.totalArmiesCount += count;
                    return;
                }
            }
        }
    }

    let leaders = [];

    for (let command of commands) {
        if (command.includes("arrives")) {
            let name = command.slice(0, command.indexOf("arrives") - 1);
            leaders.push(new Leader(name, ""));
        } else if (command.includes("defeated")) {
            let name = command.slice(0, command.indexOf("defeated") - 1);
            let leaderIndex = getLeaderIndex(name, leaders);
            if (leaderIndex !== -1) {
                leaders.splice(leaderIndex, 1);
            }
        } else if (command.includes(":") && command.includes(",")) {
            let [leaderName, armyData] = command.split(": ");
            let leaderIndex = getLeaderIndex(leaderName, leaders);
            if (leaderIndex !== -1) {
                let [armyName, count] = armyData.split(", ");
                leaders[leaderIndex].addArmy(new Army(armyName, Number(count)));
            }
        } else if (command.includes("+")) {
            let [armyName, count] = command.split(" + ");
            addCountToArmyIfExists(armyName, Number(count), leaders);
        }
    }

    for (let leader of leaders.sort((a, b) => b.totalArmiesCount - a.totalArmiesCount)) {
        leader.printInfo();
    }
}

solve(['Rick Burr arrives',
    'Findlay arrives',
    'Rick Burr: Juard, 1500',
    'Wexamp arrives',
    'Findlay: Wexamp, 34540',
    'Wexamp + 340',
    'Wexamp: Britox, 1155',
    'Wexamp: Juard, 43423']);