movie_name = ""
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while movie_name != "Finish":
    movie_name = input()
    if movie_name != "Finish":
        seats = int(input())
        full_seats = 0
        for i in range(seats):
            ticket_type = input()
            if ticket_type == "End":
                break
            full_seats += 1
            if ticket_type == "student":
                student_tickets += 1
            elif ticket_type == "standard":
                standard_tickets += 1
            else:
                kid_tickets += 1

        print(f"{movie_name} - {(full_seats / seats) * 100:.2f}% full.")

total_tickets = student_tickets + standard_tickets + kid_tickets

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
