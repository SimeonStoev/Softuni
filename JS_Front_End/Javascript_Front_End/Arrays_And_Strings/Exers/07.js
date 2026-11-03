function findSubstring(word, str) {
    let regex = new RegExp(String.raw`\b${word}\b`, "i");
    if (regex.test(str)) {
        console.log(word);
    } else {
        console.log(`${word} not found!`);
    }
}

findSubstring('javascript',
    'JavaScript is the best programming language'
);

findSubstring('python',
    'JavaScript is the best programming language'
);