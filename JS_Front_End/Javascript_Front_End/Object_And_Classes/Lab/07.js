function addressBook(addresses) {
    let addressBook = {};
    for (let personData of addresses) {
        let [name, address] = personData.split(":");
        addressBook[name] = address;
    }

    let addressBookList = Object.entries(addressBook);

    addressBookList.sort((a, b) => a[0].localeCompare(b[0]));

    for (let personAddress of addressBookList) {
        console.log(`${personAddress[0]} -> ${personAddress[1]}`);
    }
}

addressBook(['Tim:Doe Crossing',
    'Bill:Nelson Place',
    'Peter:Carlyle Ave',
    'Bill:Ornery Rd']
);