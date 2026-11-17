function solve() {
  //TODO
  const text = document.getElementById("text").value;
  const type = document.getElementById("naming-convention").value;
  const capitalize = (word) => word[0].toUpperCase() + word.slice(1).toLowerCase();
  let lowerCaseTextList = text.toLowerCase().split(" ");
  let result = "";

  if (type === "Camel Case") {
    result = lowerCaseTextList.map((word, i) => i === 0 ? word : capitalize(word)).join("");
  } else if (type === "Pascal Case") {
    result = lowerCaseTextList.map(capitalize).join("");
  } else {
    result = "Error!";
  }

  let resultEl = document.getElementById("result");
  resultEl.textContent = result;
}