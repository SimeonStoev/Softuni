function pyramidBuilder(base, increment) {
    let pyramidSteps = 0;
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;
    let pyramidBase = base;
    const step = 2;

    while (pyramidBase > 0) {
        pyramidSteps++;

        if (pyramidBase - step <= 0) {
            gold = (pyramidBase ** 2) * increment;
        } else {
            stone += ((pyramidBase - 2) ** 2) * increment;
            let outerFacade = ((pyramidBase * 4) - 4) * increment;
            if (pyramidSteps % 5 === 0) {
                lapis += outerFacade;
            } else {
                marble += outerFacade;
            }
        }

        pyramidBase -= 2;
    }
    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(pyramidSteps * increment)}`);

}

pyramidBuilder(23, 0.5);