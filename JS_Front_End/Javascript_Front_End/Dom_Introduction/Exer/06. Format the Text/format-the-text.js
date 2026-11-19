function solve() {
  // TODO
  function filterInputSentences(sentence) {
    const regex = /[a-zA-Z]/g;
    return regex.test(sentence);
  }

  const input = document.getElementById('input').value;
  const sentences = input.split(". ").filter(filterInputSentences);
  let outputEl = document.getElementById("output");

  let sentenceNumber = 0;
  let currPar = [];
  let resultEl = "";
  for (let sentence of sentences) {
    sentenceNumber++;
    currPar.push(sentence.trim());
    if (sentenceNumber % 3 === 0) {
      resultEl += `<p>${currPar.join(". ")}</p>`;
      currPar = [];
    }
  }

  if (sentenceNumber % 3 !== 0) {
    resultEl += `<p>${currPar.join(". ")}</p>`;
  }

  outputEl.innerHTML = resultEl;
}