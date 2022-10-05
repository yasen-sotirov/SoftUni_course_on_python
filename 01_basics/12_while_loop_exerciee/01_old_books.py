searched_book = input()
current_book = input()
book_counter = 0
book_is_found = False

while current_book != 'No More Books':
    if current_book == searched_book:
        book_is_found = True
        break
    book_counter += 1
    current_book = input()

if book_is_found:
    print(f'You checked {book_counter} books and found it.')
else:
    print("The book you search is not here!")
    print(f'You checked {book_counter} books.')
