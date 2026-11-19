function solve() {
    //TODO
    const theadEl = document.querySelectorAll("thead tr th");
    let visibility = [];

    for (let th of theadEl) {
        let input = th.querySelector("input");
        visibility.push({ name: input.name, visible: input.checked });
    }
    let employees = [];
    for (let tr of document.querySelectorAll("tbody tr")) {
        let objectData = {};
        const td = tr.querySelectorAll("td");
        for (let i = 0; i < td.length; i++) {
            if (visibility[i].visible) {
                objectData[visibility[i].name] = td[i].textContent;
            }
        }
        if (Object.keys(objectData).length > 0) {
            employees.push(JSON.stringify(objectData));
        }
    }

    let textAreaEl = document.getElementById("output");
    textAreaEl.value = `[${employees.join(",")}]`;
}

// Examples of creating Employee object strings
// 'employee: "Poole, Tracy", department: "Facilities/Engineering"'

// '{employee: "Poole, Tracy", department: "Facilities/Engineering"}'