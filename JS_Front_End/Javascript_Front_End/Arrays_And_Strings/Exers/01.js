function rotateList(list, n) {
    /*
    for (let i = 1; i <= n; i++) {
        let elem = list.shift();
        list.push(elem);
    }

    console.log(list.join(" "))
    */

    n = n % list.length;
    rotateArray = [...list.slice(n), ...list.slice(0, n)];
    console.log(rotateArray.join(" "))
}

rotateList([51, 47, 32, 61, 21], 2);