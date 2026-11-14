function solve(list) {
    class Flight {
        constructor(name, destination) {
            this.name = name;
            this.destination = destination;
            this.status = "";
        }

        changeStatus(newStatus) {
            this.status = newStatus;
        }

        print() {
            console.log(`{ Destination: '${this.destination}', Status: '${this.status}' }`);
        }
    }

    function changeFlightStatus(flightName, newStatus, flights) {
        for (let flight of flights) {
            if (flightName === flight.name) {
                flight.changeStatus(newStatus);
            }
        }
    }

    let flightsData = list[0];
    let changedFlights = list[1];
    let flightStatus = list[2][0];

    let flights = [];

    for (let flight of flightsData) {
        let arr = flight.split(" ");
        let name = arr[0];
        let destinaion = arr.slice(1).join(" ");
        flights.push(new Flight(name, destinaion));
    }

    for (let changedFlight of changedFlights) {
        let [name, status] = changedFlight.split(" ");
        changeFlightStatus(name, status, flights);
    }

    if (flightStatus === "Ready to fly") {
        for (let flight of flights) {
            if (flight.status === "") {
                flight.changeStatus("Ready to fly");
                flight.print();
            }
        }
    } else {
        for (let flight of flights) {
            if (flight.status !== "") {
                flight.print();
            }
        }
    }
}

solve([['WN269 Delaware',
    'FL2269 Oregon',
    'WN498 Las Vegas',
    'WN3145 Ohio',
    'WN612 Alabama',
    'WN4010 New York',
    'WN1173 California',
    'DL2120 Texas',
    'KL5744 Illinois',
    'WN678 Pennsylvania'],
['DL2120 Cancelled',
    'WN612 Cancelled',
    'WN1173 Cancelled',
    'SK330 Cancelled'],
['Ready to fly']
]
);