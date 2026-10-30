function isLeapYear(year) {
    if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
        console.log("yes");
    } else {
        console.log("no");
    }
}

isLeapYear(1984); // yes
isLeapYear(2003); // no
isLeapYear(4); // yes