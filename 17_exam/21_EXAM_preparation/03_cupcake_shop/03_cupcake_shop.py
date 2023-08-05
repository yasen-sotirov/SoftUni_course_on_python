def stock_availability(flavors_list, command, *args):
    if command == "delivery":
        for element in args:
            flavors_list.append(element)

    elif command == "sell":
        if isinstance(args[0], int):
            flavor_to_remove = args[0]
            for _ in range(flavor_to_remove):
                flavors_list.pop(0)

        elif isinstance(args[0], str):
            ordered_flavor = args[0]
            if ordered_flavor in flavors_list:
                for current_flavor in ordered_flavor:
                    while ordered_flavor in flavors_list:
                        flavors_list.remove(ordered_flavor)

        else:
            flavors_list.pop(0)

    return flavors_list


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
