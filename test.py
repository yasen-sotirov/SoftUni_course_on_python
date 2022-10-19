input_str = str(input("Enter your name: "))

# iterate over the input string using for loop

for ch in input_str:
    # return true if the character is alphabet otherwise return False

    res = ch.isalpha()

    print(ch, res)