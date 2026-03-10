number = float(input())

output_string = ""

if number == 0:
    output_string += "zero"
else:
    if 0 < abs(number) < 1:
        output_string += "small "
    elif abs(number) > 1000000:
        output_string += "large "

    if number < 0:
        output_string += "negative"
    else:
        output_string += "positive"

print(output_string)