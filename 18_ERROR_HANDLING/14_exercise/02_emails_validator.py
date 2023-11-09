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


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def is_domain_invalid(current_domain, valid_domains_list):
    result = True
    for el in valid_domains_list:
        if current_domain.endswith(el):
            result = False
            break
    return result


valid_domains = ['.com', '.bg', '.net', '.org']
while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if is_domain_invalid(domain, valid_domains):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    else:
        print("Email is valid")
