function extract(content) {
    // TODO
    let element = document.getElementById(content);
    let regex = /(?<=\().+?(?=\))/g;
    let matches = element.textContent.match(regex);
    return matches.join("; ");
}