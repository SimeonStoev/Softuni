function solve(wordList) {
    let wordAssArray = {};
    let words = wordList[0].split(" ");
    let searchWords = wordList.slice(1);
    for (let word of words) {
        wordAssArray[word] = 0;
        for (let searchWord of searchWords) {
            if (word === searchWord) {
                wordAssArray[word]++;
            }
        }
    }

    let wordsOccurs = Object.entries(wordAssArray);
    for (let wordData of wordsOccurs.sort((a, b) => b[1] - a[1])) {
        console.log(`${wordData[0]} - ${wordData[1]}`);
    }
}

solve([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
);