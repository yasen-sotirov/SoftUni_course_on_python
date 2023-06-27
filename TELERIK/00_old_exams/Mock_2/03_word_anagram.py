word = input()
number = int(input())
for _ in range(number):
    example_word = [x for x in input()]
    if len(word) == len(example_word):
        for letter in word:
            if letter in example_word:
                example_word.remove(letter)
            else:
                print("No")
                break
        print("Yes")
    else:
        print("No")

