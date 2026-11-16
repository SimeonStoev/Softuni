function solve(storeProvisions, storeDelivery) {
    class Product {
        constructor(name, quantity) {
            this.name = name;
            this.quantity = quantity;
        }

        print() {
            console.log(`${this.name} -> ${this.quantity}`);
        }
    }

    function getProductDeliveryIndexIfExists(productName, products) {
        for (let i = 0; i < products.length; i++) {
            if (products[i].name === productName) {
                return i;
            }
        }
        return -1;
    }

    let storeProducts = [];

    for (let i = 0; i < storeProvisions.length; i += 2) {
        storeProducts.push(new Product(storeProvisions[i], Number(storeProvisions[i + 1])));
    }

    for (let i = 0; i < storeDelivery.length; i += 2) {
        let deliveryProduct = storeDelivery[i];
        let deliveryQuantity = Number(storeDelivery[i + 1]);

        let index = getProductDeliveryIndexIfExists(deliveryProduct, storeProducts);
        if (index === -1) {
            storeProducts.push(new Product(deliveryProduct, deliveryQuantity));
        } else {
            storeProducts[index].quantity += deliveryQuantity;
        }
    }

    for (let product of storeProducts) {
        product.print();
    }
}

solve([
    'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
],
    [
        'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ]
);