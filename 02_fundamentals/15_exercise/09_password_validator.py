"""Write a function that checks if a given password is valid.
Password validations are:
•	It should be 6 - 10 (inclusive) characters long
•	It should consist only of letters and digits
•	It should have at least 2 digits
If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:
•	"Password must be between 6 and 10 characters"
•	"Password must consist only of letters and digits"
•	"Password must have at least 2 digits"
"""


def password_validator(some_password):
    password_is_valid = True

    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False

    digit_counter = 0
    for current_digit in some_password:
        if current_digit.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    return password_is_valid


password = input()

is_valid = password_validator(password)
if is_valid:
    print("Password is valid")