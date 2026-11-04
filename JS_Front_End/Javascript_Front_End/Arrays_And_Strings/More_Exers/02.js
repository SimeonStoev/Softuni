function bitcoinMining(goldPerDay) {
    let bitcoinsCount = 0;
    let firstDayOfPurchuaseBitcoin = 0;
    let totalMoney = 0;
    const bitcoinPrice = 11949.16;
    const goldPricePerGram = 67.51;

    for (let i = 0; i < goldPerDay.length; i++) {
        let goldForDay = (i + 1) % 3 === 0 ? goldPerDay[i] * 0.7 : goldPerDay[i];
        totalMoney += goldForDay * goldPricePerGram;
        if (totalMoney >= bitcoinPrice) {
            if (bitcoinsCount === 0) {
                firstDayOfPurchuaseBitcoin = i + 1;
            }
            let numberOfBitcoinsToBuy = Math.floor(totalMoney / bitcoinPrice);
            if (numberOfBitcoinsToBuy > 0) {
                bitcoinsCount += numberOfBitcoinsToBuy;
                totalMoney -= bitcoinPrice * numberOfBitcoinsToBuy;
            }
        }
    }

    console.log(`Bought bitcoins: ${bitcoinsCount}`)
    if (firstDayOfPurchuaseBitcoin > 0) {
        console.log(`Day of the first purchased bitcoin: ${firstDayOfPurchuaseBitcoin}`)
    }
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`)
}

bitcoinMining([3124.15, 504.212, 2511.124]);