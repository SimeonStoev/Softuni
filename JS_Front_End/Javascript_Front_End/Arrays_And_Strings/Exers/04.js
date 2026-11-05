function sortNumbers(list) {
    let returnList = [];
    list.sort((a, b) => a - b);

    let left = 0, rigth = list.length - 1;

    while (left <= rigth) {
        returnList.push(list[left]);
        left++;
        if (left <= rigth) {
            returnList.push(list[rigth]);
            rigth--;
        }

    }

    /*
    const endIndex = list.length / 2;

    for (let i = 0; i < endIndex; i++) {
        returnList.push(list[i]);
        if (i !== list.length - 1 - i) {
            returnList.push(list[list.length - 1 - i]);
        }
    }
        */

    return returnList;
}

console.log(sortNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));

console.log(sortNumbers([1, 2, 3]));