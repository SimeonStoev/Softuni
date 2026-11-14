function convertToJson(firstName, lastName, hairColor) {
    let object = { name: firstName, lastName: lastName, hairColor: hairColor };
    console.log(JSON.stringify(object));
}

convertToJson('George', 'Jones', 'Brown');