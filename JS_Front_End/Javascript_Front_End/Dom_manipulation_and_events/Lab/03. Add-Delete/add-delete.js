function addItem() {
    // TODO
    const elementToAdd = document.getElementById("newItemText");
    const ulEl = document.getElementById("items");
    const liEl = document.createElement("li");
    liEl.innerHTML = `${elementToAdd.value}<a href="#">[Delete]</a>`;
    ulEl.appendChild(liEl);

    const linkEl = liEl.querySelector("a");
    linkEl.addEventListener("click", deleteLink);

    function deleteLink(e) {
        e.target.parentElement.remove();
    }

    elementToAdd.value = "";
}
