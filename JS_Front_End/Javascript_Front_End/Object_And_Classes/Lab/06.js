function meetings(meetingList) {
    let meetList = {};
    for (let meeting of meetingList) {
        let [day, name] = meeting.split(" ");
        if (day in meetList) {
            console.log(`Conflict on ${day}!`);
        } else {
            meetList[day] = name;
            console.log(`Scheduled for ${day}`);
        }
    }

    for (let day of Object.keys(meetList)) {
        console.log(`${day} -> ${meetList[day]}`);
    }
}

meetings(['Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim']
);