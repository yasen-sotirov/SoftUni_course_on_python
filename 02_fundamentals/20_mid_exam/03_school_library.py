shelf = input().split("&")
command = input().split(" | ")

while len(command) > 1:
    action = command[0]
    book_name = command[1]
    if len(command) > 2:
        book_name_2 = command[2]
        if "Swap Book" in action:
            if book_name in shelf and book_name_2 in shelf:
                index_book_1 = shelf.index(book_name)
                index_book_2 = shelf.index(book_name_2)
                shelf[index_book_1], shelf[index_book_2] = shelf[index_book_2], shelf[index_book_1]

    if "Add Book" in action:
        if book_name not in shelf:
            shelf.insert(0, book_name)

    elif "Take Book" in action:
        if book_name in shelf:
            shelf.remove(book_name)

    elif "Insert Book" in action:
        if book_name not in shelf:
            shelf.append(book_name)

    elif "Check Book" in action:
        index = int(book_name)
        if index in range(len(shelf)):
            print(shelf[index])

    command = input().split(" | ")

print(", ".join(shelf))
