numbers = [int(x) for x in input().split()]

positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]

sum_positive_numbers = sum(positive_numbers)
sum_negative_numbers = sum(negative_numbers)
print(sum_negative_numbers)
print(sum_positive_numbers)
if abs(sum_negative_numbers) > sum_positive_numbers:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
