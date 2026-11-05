function replaceTemplateWithWords(words, sentence) {
    let wordsList = words.split(", ");

    let result = sentence.replace(/\*+/g, (match) => {
        let index = wordsList.findIndex(word => word.length === match.length);

        if (index !== -1) {
            return wordsList.splice(index, 1)[0];
        }

        return match;
    });

    console.log(result);
}


replaceTemplateWithWords('great',
    'softuni is ***** place for learning new programming languages'
);

replaceTemplateWithWords('great, place',
    'softuni is ***** *****'
);