class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split()
    emails.append(Email(command[0], command[1], command[2]))

for index in [int(x) for x in input().split(", ")]:
    emails[index].send()

for email in emails:
    print(email.get_info())