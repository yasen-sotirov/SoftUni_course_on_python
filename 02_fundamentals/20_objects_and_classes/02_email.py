class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


emails_list = []
data = input()
while not data == "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails_list.append(email)
    data = input()

indexes = [int(el) for el in input().split(", ")]

for index in indexes:
    emails_list[index].send()

for email in emails_list:
    print(email.get_info())