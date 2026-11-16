function solve(commands) {
    class Student {
        constructor(username, email, credits) {
            this.username = username;
            this.email = email;
            this.credits = credits;
        }

        print() {
            console.log(`--- ${this.credits}: ${this.username}, ${this.email}`);
        }
    }

    class Course {
        constructor(name, capacity) {
            this.name = name;
            this.capacity = capacity;
            this.students = [];
        }

        addStudent(student) {
            if (this.capacity > 0) {
                this.students.push(student);
                this.capacity--;
            }
        }

        print() {
            console.log(`${this.name}: ${this.capacity} places left`);
            for (let student of this.students.sort((a, b) => b.credits - a.credits)) {
                student.print();
            }
        }
    }

    function getCourseIndex(courseName, courses) {
        for (let i = 0; i < courses.length; i++) {
            if (courses[i].name === courseName) {
                return i;
            }
        }
        return -1;
    }

    let courses = [];

    for (let command of commands) {
        if (command.includes(":")) {
            let [courseName, capacity] = command.split(": ");
            let courseIndex = getCourseIndex(courseName, courses);
            if (courseIndex !== -1) {
                courses[courseIndex].capacity += Number(capacity);
            } else {
                courses.push(new Course(courseName, Number(capacity)));
            }
        } else {
            let regex = /(?<username>\w+)\[(?<credits>\d+)\] with email (?<email>[\w@.]+) joins (?<course>.+)/;
            let match = command.match(regex);

            let username = match.groups.username;
            let credits = Number(match.groups.credits);
            let email = match.groups.email;
            let course = match.groups.course;

            let courseIndex = getCourseIndex(course, courses);

            if (courseIndex !== -1) {
                courses[courseIndex].addStudent(new Student(username, email, credits));
            }
        }
    }

    for (let course of courses.sort((a, b) => b.students.length - a.students.length)) {
        course.print();
    }
}

solve(['JavaBasics: 15',
    'user1[26] with email user1@user.com joins JavaBasics',
    'user2[36] with email user11@user.com joins JavaBasics',
    'JavaBasics: 5',
    'C#Advanced: 5',
    'user1[26] with email user1@user.com joins C#Advanced',
    'user2[36] with email user11@user.com joins C#Advanced',
    'user3[6] with email user3@user.com joins C#Advanced',
    'C#Advanced: 1',
    'JSCore: 8',
    'user23[62] with email user23@user.com joins JSCore']
);