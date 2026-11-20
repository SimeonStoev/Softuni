function solve() {
   function clearPreviousSearch(towns) {
      for (let town of towns) {
         town.style.textDecoration = "initial";
         town.style.fontWeight = "Normal";
      }
   }
   // TODO
   const searchValue = document.querySelector("#searchText").value;
   let towns = document.querySelectorAll("#towns li");
   let result = document.getElementById("result");
   let foundResults = 0;

   clearPreviousSearch(towns);
   if (searchValue === "") {
      result.textContent = "";
      return;
   }

   for (let town of towns) {
      if (town.textContent.includes(searchValue)) {
         town.style.textDecoration = "underline";
         town.style.fontWeight = "bold";
         foundResults++;
      }
   }

   result.textContent = `${foundResults} matches found`;
}