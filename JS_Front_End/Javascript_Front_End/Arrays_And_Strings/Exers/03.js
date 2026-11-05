function sortList(list) {
    let counter = 0;
    list.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
    for (elem of list) {
        counter++;
        console.log(`${counter}.${elem}`)
    }
}

sortList(["John", "Bob", "Christina", "Ema"]);