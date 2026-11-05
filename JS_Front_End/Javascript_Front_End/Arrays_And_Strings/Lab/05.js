function setCensoredWord(string, censoredWord) {
    censor = "*".repeat(censoredWord.length);
    censoredString = string.replaceAll(censoredWord, censor);
    console.log(censoredString);
}

setCensoredWord('Find the hidden word', 'hidden');