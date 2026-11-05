function login(input) {
    let countTry = 0;
    let username = input[0];

    for (let i = 1; i < input.length; i++) {
        countTry++;
        let password = input[i];

        let reversedPassword = password.split("").reverse().join("");
        if (username === reversedPassword) {
            console.log(`User ${username} logged in.`);
            break;
        } else {
            if (countTry < 4) {
                console.log("Incorrect password. Try again.");
            }
        }

        if (countTry === 4) {
            console.log(`User ${username} blocked!`);
            break;
        }

    }
}

login(['sunny', 'rainy', 'cloudy', 'sunny', 'not sunny']);