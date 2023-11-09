user_name = input()
user_password = input()
data = input()

while user_password != data:
    data = input()

print(f'Welcome {user_name}!')
