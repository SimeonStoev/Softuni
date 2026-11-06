function printGradeDescr(grade) {
    let gradeDescr = "";

    if (grade < 3) {
        gradeDescr = `Fail (${Math.floor(grade)})`;
    } else if (grade >= 3 && grade < 3.50) {
        gradeDescr = `Poor (${grade.toFixed(2)})`;
    } else if (grade >= 3.50 && grade < 4.50) {
        gradeDescr = `Good (${grade.toFixed(2)})`;
    } else if (grade >= 4.50 && grade < 5.50) {
        gradeDescr = `Very good (${grade.toFixed(2)})`;
    } else if (grade >= 5.50) {
        gradeDescr = `Excellent (${grade.toFixed(2)})`;
    } else {
        gradeDescr = "Invalid grade";
    }

    console.log(gradeDescr);
}

printGradeDescr(2.99);