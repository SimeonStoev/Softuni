function solve(lists) {
    function isListUnique(list, arrayOfLists) {
        for (let arrayList of arrayOfLists) {
            if (JSON.stringify(list) === JSON.stringify(arrayList)) {
                return false;
            }
        }
        return true;
    }

    let arrays = [];

    for (let list of lists) {
        let sortedList = JSON.parse(list).sort((a, b) => b - a);
        if (isListUnique(sortedList, arrays)) {
            arrays.push(sortedList);
        }
    }

    for (let array of arrays.sort((a, b) => a.length - b.length)) {
        console.log(`[${array.join(", ")}]`);
    }
}

solve(["[7.14, 7.180, 7.339, 80.099]",
    "[7.339, 80.0990, 7.140000, 7.18]",
    "[7.339, 7.180, 7.14, 80.099]"]
);