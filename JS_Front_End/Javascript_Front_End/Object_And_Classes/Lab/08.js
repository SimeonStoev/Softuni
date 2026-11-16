function catsMeow(cats) {
    class Cat {
        constructor(catName, age) {
            this.catName = catName;
            this.age = age;
        }

        meow() {
            console.log(`${this.catName}, age ${this.age} says Meow`);
        }
    }

    for (let catData of cats) {
        let [name, age] = catData.split(" ");
        let cat = new Cat(name, age);
        cat.meow();
    }
}

catsMeow(['Mellow 2', 'Tom 5']);