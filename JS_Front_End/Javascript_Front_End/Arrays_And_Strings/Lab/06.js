function countWordOccursInString(str, word) {
    const regexp = /\w+/g;
    let words = str.match(regexp);
    console.log(words.filter(elem => elem === word).length)
}

countWordOccursInString('softuni is great place for learning new programming languages',
    'softuni');