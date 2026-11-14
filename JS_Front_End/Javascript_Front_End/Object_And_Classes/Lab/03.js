function convertJSONToObject(json) {
    let jsonObject = JSON.parse(json);

    for (let key of Object.keys(jsonObject)) {
        console.log(`${key}: ${jsonObject[key]}`);
    }
}

convertJSONToObject('{"name": "George", "age": 40, "town": "Sofia"}');