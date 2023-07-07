"""" You will receive a single integer number between 0 and 100 (inclusive)
divisible by 10 without remainder (0, 10, 20, 30...).
Your task is to create a function that returns a loading bar depending on the number
you have received in the input. Print the result on the console. """


number = int(input())
loader = []

for num in range(number // 10):
    loader.append('%')

for dot in range(10 - number // 10):
    loader.append(".")

loader_bar = "".join(loader)

if number < 100:
    print(f"{number / 100:.0%} {loader_bar.join('[]')}")
    print('Still loading...')
else:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
