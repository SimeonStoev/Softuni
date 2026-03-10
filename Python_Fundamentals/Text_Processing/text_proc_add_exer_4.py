reverse_morse_codes = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "|"
}

decode_table = {v: k for k, v in reverse_morse_codes.items()}


def encode(s):
    return " ".join(reverse_morse_codes[x] for x in s)


def decode(encoded):
    symbols = encoded.split()
    return "".join(decode_table[x] for x in symbols)


morse_code_string = input()
print(decode(morse_code_string))
