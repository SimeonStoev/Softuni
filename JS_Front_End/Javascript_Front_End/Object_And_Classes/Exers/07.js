function solve(str) {
    let countsElems = {};
    for (let word of str.split(" ")) {
        let wordLower = word.toLowerCase();
        countsElems[wordLower] = countsElems[wordLower] ? countsElems[wordLower] + 1 : 1;
    }

    let oddWordsOccurs = Object.entries(countsElems).filter((a) => a[1] % 2 !== 0).sort((a, b) => b[1] - a[1]);
    let result = [];

    for (let word of oddWordsOccurs) {
        result.push(word[0]);
    }

    console.log(result.join(" "));
}

solve('Cake IS SWEET is Soft CAKE sweet Food');