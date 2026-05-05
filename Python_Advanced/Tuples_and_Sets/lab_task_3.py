number_of_elems = int(input())
unique_elements = set()

for _ in range(number_of_elems):
    element = input()
    unique_elements.add(element)

print("\n".join(unique_elements))