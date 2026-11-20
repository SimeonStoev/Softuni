function sumTable() {
    // TODO
    let sum = 0;
    for (let elem of document.querySelectorAll('table tr td:nth-child(2)')) {
        if (elem.id !== "sum") {
            sum += Number(elem.textContent);
        }
    }

    document.getElementById("sum").textContent = sum.toFixed(2);
}