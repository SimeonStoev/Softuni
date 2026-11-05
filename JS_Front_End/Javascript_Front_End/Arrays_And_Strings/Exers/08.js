function pascalCaseSplit(str) {
    normalStr = str.replace(/([A-Z])/g, ' $1').slice(1);

    console.log(normalStr.split(" ").join(", "));
}


pascalCaseSplit('ThisIsSoAnnoyingToDo');