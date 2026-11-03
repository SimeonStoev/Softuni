function printEveryNthElem(list, n) {
    let resultList = [];
    for (let i = 0; i < list.length; i += n) {
        resultList.push(list[i]);
    }
    return resultList;
}

console.log(printEveryNthElem(['1',
    '2',
    '3',
    '4',
    '5'],
    6
));