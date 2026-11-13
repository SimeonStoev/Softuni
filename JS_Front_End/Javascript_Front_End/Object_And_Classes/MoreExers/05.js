function solve(studentsData) {
    class Student {
        constructor(name, grade, avarageScore) {
            this.name = name;
            this.grade = grade;
            this.avarageScore = avarageScore;
        }

        print() {
            console.log(`${this.name} - ${this.grade} - ${this.avarageScore}`);
        }
    }

    let students = [];

    for (let studentData of studentsData) {
        let [nameData, gradeData, scoreData] = studentData.split(", ");
        let name = nameData.split(": ")[1];
        let grade = Number(gradeData.split(": ")[1]);
        let score = Number(scoreData.split(": ")[1]);
        if (score >= 3) {
            students.push(new Student(name, grade + 1, score));
        }
    }

    let currGrade = 0;
    for (let student of students.sort((a, b) => a.grade - b.grade)) {
        if (currGrade !== student.grade) {
            currGrade = student.grade;
            let studentNames = [];
            let averageScore = 0;
            let numberOfStudents = 0;
            for (let std of students.filter(a => a.grade === currGrade)) {
                studentNames.push(std.name);
                averageScore += std.avarageScore;
                numberOfStudents++;
            }


            console.log(`${currGrade} Grade`);
            console.log(`List of students: ${studentNames.join(", ")}`);
            console.log(`Average annual score from last year: ${(averageScore / numberOfStudents).toFixed(2)}`);
            console.log("");
        }
    }
}

solve([
    'Student name: George, Grade: 5, Graduated with an average score: 2.75',
    'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
    'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
    'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
    'Student name: John, Grade: 9, Graduated with an average score: 2.90',
    'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
    'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
]
);