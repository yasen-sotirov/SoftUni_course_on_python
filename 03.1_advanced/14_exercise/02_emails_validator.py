""" 2.	Email Validator
You will be given some emails until you receive the command "End". C
reate the following custom exceptions to validate the emails:
•	NameTooShortError - raise it when the name in the email is less than
    or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
•	MustContainAtSymbolError - raise it when there is no "@" in the email
•	InvalidDomainError - raise it when the domain of the email is invalid
    (valid domains are: .com, .bg, .net, .org)

When an error is encountered, raise it with an appropriate message:
•	NameTooShortError - "Name must be more than 4 characters"
•	MustContainAtSymbolError - "Email must contain @"
•	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"

Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one

    Examples
    Input
abc@abv.bg

    Output
Traceback (most recent call last):
  File ".\email_validator.py", line 20, in <module>
    raise NameTooShort("Name must be more than 4 characters")
__main__.NameTooShort: Name must be more than 4 characters

"""


