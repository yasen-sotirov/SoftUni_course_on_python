"""" Write a program that reads a single string with numbers separated by comma and space ", ".
Print the indices of all even numbers."""


nums = [int(el) for el in input().split(", ")]
print([index for index in range(len(nums)) if nums[index] % 2 == 0])
