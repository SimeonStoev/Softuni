function cookingNumbers(numbStr, operation1, operation2, operation3, operation4, operation5) {
    let number = Number(numbStr);
    let operations = [operation1, operation2, operation3, operation4, operation5];
    for (let operation of operations) {
        switch (operation) {
            case 'chop':
                number /= 2;
                break;
            case 'dice':
                number = Math.sqrt(number);
                break;
            case 'spice':
                number += 1;
                break;
            case 'bake':
                number *= 3;
                break;
            case 'fillet':
                number *= 0.8;
                break;
        }
        console.log(number);
    }
}

cookingNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
