"""" Create class Email. The __init__ method should receive sender,
receiver and a content. It should also have a default set to False
attribute called is_sent. The class should have two additional methods:
•	send() - sets the is_sent attribute to True
•	get_info() - returns the following string: "{sender} says to {receiver}: {content}.
Sent: {is_sent}"
You will receive some information (separated by a single space) until
you receive the command "Stop". The first element will be the sender,
the second one – the receiver, and the third one – the content.
On the final line, you will be given the indices of the sent emails separated
by comma and space ", ".
Call the send() method for the given indices of emails.
For each email, call the get_info() method.
"""


class Email:
    __list = []                                         # клас атрибут

    def __init__(self, sender, receiver, content):      # конструктор
        self.sender = sender                            # инстанс атрибут
        self.receiver = receiver                        # инстанс атрибут
        self.content = content                          # инстанС атрибут
        self.is_sent = False                            # инстанс атрибут

    def send(self):         # когато функцията е в class се казва метод
        self.is_sent = True

    def get_info(self):         # метод
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


emails_list = []
data = input()
while not data == "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails_list.append(email)
    data = input()

indexes_for_send_email = [int(el) for el in input().split(", ")]

for index in indexes_for_send_email:
    emails_list[index].send()

for email in emails_list:
    print(email.get_info())
