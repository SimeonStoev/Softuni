function printAllHashTagWords(str) {
    hashTagWords = str.match(/#[A-Za-z]+/g);
    for (word of hashTagWords) {
        console.log(word.slice(1));
    }
}

printAllHashTagWords('The symbol # is known #variously in English-speaking #regions as the #number sign');