function solve(browserObject, commands) {

    function isSiteOpen(site, openSites) {
        for (let openSite of openSites) {
            if (site === openSite) {
                return true;
            }
        }
        return false;
    }

    const specialCommand = "Clear History and Cache";

    for (let command of commands) {
        if (command === specialCommand) {
            browserObject["Recently Closed"] = [];
            browserObject["Open Tabs"] = [];
            browserObject["Browser Logs"] = [];
        } else {
            let arr = command.split(" ");
            let com = arr[0];
            let site = arr.slice(1).join(" ");

            if (com === "Open") {
                browserObject["Open Tabs"].push(site);
                browserObject["Browser Logs"].push(command);
            } else if (com === "Close" && isSiteOpen(site, browserObject["Open Tabs"])) {
                let openSiteIndex = browserObject["Open Tabs"].indexOf(site);
                browserObject["Open Tabs"].splice(openSiteIndex, 1);
                browserObject["Recently Closed"].push(site);
                browserObject["Browser Logs"].push(command);
            }

        }
    }

    console.log(browserObject["Browser Name"]);
    console.log(`Open Tabs: ${browserObject["Open Tabs"].join(", ")}`);
    console.log(`Recently Closed: ${browserObject["Recently Closed"].join(", ")}`);
    console.log(`Browser Logs: ${browserObject["Browser Logs"].join(", ")}`);
}

solve({
    "Browser Name": "Mozilla Firefox",
    "Open Tabs": ["YouTube"],
    "Recently Closed": ["Gmail", "Dropbox"],
    "Browser Logs": ["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]
},
    ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]);