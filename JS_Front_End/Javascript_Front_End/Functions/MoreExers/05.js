function printDNAChain(n) {
    const dna = "ATCGTTAGGG";
    const patterns = [
        (a, b) => `**${a}${b}**`,
        (a, b) => `*${a}--${b}*`,
        (a, b) => `${a}----${b}`,
        (a, b) => `*${a}--${b}*`
    ];

    for (let i = 0; i < n; i++) {
        let patternIndex = i % 4;

        let a = dna[i * 2 % dna.length];
        let b = dna[(i * 2 + 1) % dna.length]

        console.log(patterns[patternIndex](a, b));
    }
}

printDNAChain(10);