function solve(list) {
    let products = {};

    for (let productData of list) {
        let [product, price] = productData.split(" : ");
        products[product] = price;
    }

    let category = "";
    for (let product of Object.entries(products).sort((a, b) => a[0].localeCompare(b[0]))) {
        if (category !== product[0][0]) {
            category = product[0][0];
            console.log(category);
        }
        console.log(`  ${product[0]}: ${product[1]}`);
    }
}

solve([
    'Omlet : 5.4',
    'Shirt : 15',
    'Cake : 59'
]
);