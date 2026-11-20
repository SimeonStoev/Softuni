function solve() {
   //TODO
   function resetTableRowsClass(tableRows) {
      for (let row of tableRows) {
         row.classList.remove("select");
      }
   }

   const searchValue = document.getElementById("searchField").value;
   let tableRows = document.querySelectorAll("tbody tr");
   resetTableRowsClass(tableRows);
   if (searchValue === "") {
      return;
   }

   for (let row of tableRows) {
      for (let cell of row.querySelectorAll("td")) {
         if (cell.textContent.includes(searchValue)) {
            row.classList.add("select");
            break;
         }
      }
   }
}