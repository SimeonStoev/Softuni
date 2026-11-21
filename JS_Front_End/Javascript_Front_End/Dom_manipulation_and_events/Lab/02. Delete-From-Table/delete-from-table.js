function deleteByEmail() {
    //TODO
    const email = document.querySelector("label input").value;
    const resultEl = document.getElementById("result");
    let result = "Not found."

    let tableRowsElms = document.querySelectorAll("tbody tr");

    for (let row of tableRowsElms) {
        const rowEmail = row.querySelector("td:nth-child(2)").textContent;
        if (rowEmail === email) {
            result = "Deleted."
            row.remove();
        }
    }

    resultEl.textContent = result;
}
