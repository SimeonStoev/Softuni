function colorize() {
    //TODO
    let tableRows = document.querySelectorAll("tbody tr");
    for (let row = 0; row < tableRows.length; row++) {
        if ((row + 1) % 2 === 0) {
            tableRows[row].style.backgroundColor = "Teal";
        }
    }
}