# comments are here for guidance
# you can delete them before the demo

def get_valid_string(input_name, min_length):
    while True:
        print(f'Enter <{input_name}>, at least <{min_length}> chars long')
        txt = input()
        if len(txt) >= min_length:
            return txt

# register_customer() is create by using get_valid_string()
# in turn, register_customer 
# can be used inside another function to build more complex program

def register_customer():
    first_name = get_valid_string('First Name', 2) 
    last_name = get_valid_string('Last Name', 2)
    city = get_valid_string('City Name', 3)

    print(f'Customer created: {first_name} {last_name}')
    print(f'Residence: {city}')

register_customer()