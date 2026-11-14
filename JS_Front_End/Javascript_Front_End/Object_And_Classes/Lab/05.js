function phoneBook(phones) {
    let phoneList = {};
    for (let phoneData of phones) {
        let [name, phone] = phoneData.split(" ");
        phoneList[name] = phone;
    }

    for (let key of Object.keys(phoneList)) {
        console.log(`${key} -> ${phoneList[key]}`);
    }
}

phoneBook(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']
);