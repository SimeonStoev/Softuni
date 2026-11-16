function extractText() {
    // TODO
    let listData = document.querySelectorAll("#items li");
    let listDataArray = Array.from(listData);
    let result = "";
    for (let listEl of listDataArray) {
        result += listEl.textContent + " ";
    }

    let textarea = document.getElementById("result");
    textarea.textContent = result.trim();
}