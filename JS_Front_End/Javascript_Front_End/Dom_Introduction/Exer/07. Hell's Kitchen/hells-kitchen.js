function solve() {
    //TODO
    class Restaurant {
        constructor(name) {
            this.name = name;
            this.employees = [];
            this.averageSalary = 0;
            this.bestSalary = 0;
        }

        getAverageSalary() {
            let allSalaries = 0;
            for (let employee of this.employees) {
                allSalaries += employee.salary;
            }

            return allSalaries / this.employees.length;
        }

        getBestSalary() {
            return this.employees.sort((a, b) => b.salary - a.salary)[0].salary;
        }

        addEmployee(employee) {
            this.employees.push(employee);
        }

        getRestaurantInfo() {
            return `Name: ${this.name} Average Salary: ${this.getAverageSalary().toFixed(2)} Best Salary: ${this.getBestSalary().toFixed(2)}`;
        }

        getEmployeesInfo() {
            let result = [];
            for (let employee of this.employees.sort((a, b) => b.salary - a.salary)) {
                result.push(employee.getInfo());
            }
            return result.join(" ");
        }
    }

    class Employee {
        constructor(name, salary) {
            this.name = name;
            this.salary = salary;
        }

        getInfo() {
            return `Name: ${this.name} With Salary: ${this.salary}`;
        }
    }

    function getRestaurantIndex(restaurantName, restaurants) {
        for (let i = 0; i < restaurants.length; i++) {
            if (restaurants[i].name === restaurantName) {
                return i;
            }
        }
        return -1;
    }

    function addEmployeesToRestaurant(restaurant, employees) {
        for (let employee of employees) {
            restaurant.addEmployee(employee);
        }
    }

    const inputElValue = document.querySelector("#inputs textarea").value;
    let restData = inputElValue.match(/"[^"]+"/g).map(s => s.replaceAll('"', ''));

    let restaurants = [];

    for (let rest of restData) {
        let [restName, employeesData] = rest.split(" - ");
        const restIndex = getRestaurantIndex(restName, restaurants);
        let employees = [];
        for (let emplData of employeesData.split(", ")) {
            let [name, salary] = emplData.split(" ");
            employees.push(new Employee(name, Number(salary)));
        }

        if (restIndex === -1) {
            let newRest = new Restaurant(restName);
            restaurants.push(newRest);
            addEmployeesToRestaurant(newRest, employees);
        } else {
            addEmployeesToRestaurant(restaurants[restIndex], employees);
        }
    }

    restaurants = restaurants.sort((a, b) => b.getAverageSalary() - a.getAverageSalary());

    let bestRestEl = document.querySelector("#bestRestaurant p");

    let bestWorkersEl = document.querySelector("#workers p");

    bestRestEl.textContent = restaurants[0].getRestaurantInfo();
    bestWorkersEl.textContent = restaurants[0].getEmployeesInfo();

}