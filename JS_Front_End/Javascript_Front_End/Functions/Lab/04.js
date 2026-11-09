function calcPriceForProducts(product, quantity) {
    let singlePrice = 0;

    switch (product) {
        case "coffee":
            singlePrice = 1.50;
            break;
        case "water":
            singlePrice = 1;
            break;
        case "coke":
            singlePrice = 1.40;
            break;
        case "snacks":
            singlePrice = 2;
            break;
    }

    console.log((singlePrice * quantity).toFixed(2));

}

calcPriceForProducts("coffee", 2);