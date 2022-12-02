"""" Problem 2 - Fancy Barcodes
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2303#1.

Your first task is to determine if the given sequence of characters is a valid barcode or not.
Each line must not contain anything else but a valid barcode. A barcode is valid when:
•	It is surrounded by a "@" followed by one or more "#"
•	It is at least 6 characters long (without the surrounding "@" or "#")
•	It starts with a capital letter
•	It contains only letters (lower and upper case) and digits
•	It ends with a capital letter
Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
Next, you have to determine the product group of the item from the barcode.
The product group is obtained by concatenating all the digits found in the barcode.
If there are no digits present in the barcode, the default product group is "00".
Examples:
@#FreshFisH@# -> product group: 00
@###Brea0D@### -> product group: 0
@##Che4s6E@## -> product group: 46
Input
On the first line, you will be given an integer n – the count of barcodes that you will be receiving next.
On the following n lines, you will receive different strings.
Output
For each barcode that you process, you need to print a message.
If the barcode is invalid:
•	"Invalid barcode"
If the barcode is valid:
•	"Product group: {product group}"
"""
import re


number_of_barcode = int(input())

for _ in range(number_of_barcode):
    barcode = input()
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    result = re.findall(pattern, barcode)
    result_as_str = ' '.join(result)
    if result:
        pattern = r'\d'
        extract_nums = re.findall(pattern, result)
        if not extract_nums:
            print('Product group: 00')
        else:
            print(f'Product group: {"".join(extract_nums)}')
    else:
        print("Invalid barcode")
