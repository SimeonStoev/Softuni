function createLoadingBarByPercent(percent) {
    let loadingBarList = ". . . . . . . . . .".split(" ");
    for (let i = 0; i < percent / 10; i += 1) {
        loadingBarList[i] = "%";
    }
    let loadingBar = `[${loadingBarList.join("")}]`;

    if (percent === 100) {
        console.log("100% Complete!");
        console.log(loadingBar);
    } else {
        console.log(`${percent}% ${loadingBar}`);
        console.log("Still loading...");
    }
}

createLoadingBarByPercent(100);