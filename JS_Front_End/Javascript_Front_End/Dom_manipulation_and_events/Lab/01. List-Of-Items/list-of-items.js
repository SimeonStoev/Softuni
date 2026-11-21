function addItem() {
    //TODO
    const inputElValue = document.getElementById("newItemText").value;
    const ulEl = document.getElementById("items");
    const liEl = document.createElement("li");
    liEl.textContent = inputElValue;
    ulEl.appendChild(liEl);
}
