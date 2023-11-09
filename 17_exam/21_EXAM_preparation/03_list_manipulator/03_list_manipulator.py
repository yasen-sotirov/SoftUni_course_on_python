def list_manipulator(start_list, command, position, *args):

    if command == "add":
        if position == "beginning":
            for index in range(len(args)-1, -1, -1):
                start_list.insert(0, args[index])

        elif position == "end":
            for el in args:
                start_list.append(el)

    elif command == "remove":
        if position == "beginning":
            if args:
                for el in range(args[0]):
                    start_list.pop(0)
            if not args:
                start_list.pop(0)

        elif position == "end":
            if args:
                for el in range(args[0]):
                    start_list.pop()
            elif not args:
                start_list.pop()

    return start_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
