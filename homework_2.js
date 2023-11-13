const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function convertToBinary(decimalNumber) {

    let number = parseInt(decimalNumber);

    if (isNaN(number) || number < 0) {
        console.error("Chyba: Zadali ste neplatný vstup. Zadajte prosím prirodzené číslo alebo nulu.");
        return
    }

    if (number === 0) {
        return "0"
    }

    let binary = "";

    while (number > 0) {
        binary = (number % 2) + binary;
        number = Math.floor(number / 2);
    }

    return binary
}

rl.question("Zadaj prirodzené číslo alebo nulu pre prevod do dvojkovej sústavy: ", function (input) {
    const output = convertToBinary(input);

    console.log(`Dvojkový zápis čísla ${input} je: ${output}`);
    rl.close();
});
