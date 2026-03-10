wrapping_paper_price = 5.8
fabric_price = 7.2
glue_price = 1.2

wrapping_paper = int(input())
fabric = int(input())
glue = float(input())
discount_percent = int(input())

sum = wrapping_paper * wrapping_paper_price + fabric * fabric_price + glue * glue_price

sum_with_discount = sum - sum * (discount_percent / 100)

print(f"{sum_with_discount:.3f}")