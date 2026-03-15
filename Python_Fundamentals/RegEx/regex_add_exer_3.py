import re


def decrypt_string(string_param, count):
    decrypted_string = ""
    for index in range(len(string_param)):
        decrypted_string += chr(ord(string_param[index]) - count)

    return decrypted_string


def is_message_valid(pat, message):
    return bool(re.search(pat, message))


pattern_decrypt = "[SsTtAaRr]"
pattern = r"[^@!:>-]*@([A-Za-z]+)[^@!:>-]*:([0]|[1-9][0-9]*)[^@!:>-]*!([A|D])![^@!:>-]*->(([0]|[1-9][0-9]*))[^@!:>-]*"
planets_dict = {"A": [], "D": []}
message_number = int(input())

for i in range(message_number):
    string = input()
    decrypted_chars_count = len(re.findall(pattern_decrypt, string))
    string_decrypted = decrypt_string(string, decrypted_chars_count)
    if is_message_valid(pattern, string_decrypted):
        planet_name = re.search(pattern, string_decrypted).group(1)
        attack_type = re.search(pattern, string_decrypted).group(3)
        if attack_type == "A":
            planets_dict["A"].append(planet_name)
        else:
            planets_dict["D"].append(planet_name)

attacked_planets = len(planets_dict["A"])
destroyed_planets = len(planets_dict["D"])

print(f"Attacked planets: {attacked_planets}")
for planet in sorted(planets_dict["A"]):
    print(f"-> {planet}")

print(f"Destroyed planets: {destroyed_planets}")
for planet in sorted(planets_dict["D"]):
    print(f"-> {planet}")
