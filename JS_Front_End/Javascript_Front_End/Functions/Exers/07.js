function printMatrix(number) {
    let row;
    for (let i = 0; i < number; i++) {
        row = "";
        for (let j = 0; j < number; j++) {
            row += number + " ";
        }
        console.log(row.trim());
    }
}

printMatrix(7);