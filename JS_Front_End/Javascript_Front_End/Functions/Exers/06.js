function isPasswordValid(password) {
    function isPasswordLengthOK(pass) {
        if (pass.length >= 6 && pass.length <= 10) {
            return true;
        }
        return false;
    }

    function isPasswordOfOnlyLetterAndDigits(pass) {
        const regex = /^[A-Za-z0-9]+$/g;
        return regex.test(pass);
    }

    function hasPasswordAtLeatsTwoDigits(pass) {
        const regex = /[0-9]/g;
        passNumbs = pass.match(regex);
        return passNumbs !== null && passNumbs.length >= 2;
    }

    let validPassword = true;

    if (!isPasswordLengthOK(password)) {
        validPassword = false;
        console.log("Password must be between 6 and 10 characters");
    }
    if (!isPasswordOfOnlyLetterAndDigits(password)) {
        validPassword = false;
        console.log("Password must consist only of letters and digits");
    }
    if (!hasPasswordAtLeatsTwoDigits(password)) {
        validPassword = false;
        console.log("Password must have at least 2 digits");
    }

    if (validPassword) {
        console.log("Password is valid");
    }
}

isPasswordValid('Pa$s$s');