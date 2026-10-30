function wordsUppercase(str) {
    let words = str.toUpperCase().match(/\w+/g);
    let result = "";
    for (let word of words) {
        result += word + ", ";
    }
    console.log(result.slice(0, -2));
}

wordsUppercase('hello');