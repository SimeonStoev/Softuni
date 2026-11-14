function employees(employeeList) {
    class Employee {
        constructor(name, personalNumber) {
            this.name = name;
            this.personalNumber = personalNumber;
        }

        print() {
            console.log(`Name: ${this.name} -- Personal Number: ${this.personalNumber}`);
        }
    }

    let employees = [];

    for (let employeeName of employeeList) {
        employees.push(new Employee(employeeName, employeeName.length));
    }

    for (let employee of employees) {
        employee.print();
    }
}

employees([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
]
);