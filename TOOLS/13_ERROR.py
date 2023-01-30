"ERROR HANDALING" #



"ВРЪЩА ДОПЪЛНИТЕЛНО СЪОБЩЕНИЕ"      # към съществуващ клас грешки
# b = 0
# if b == 0:
#     raise IndexError("Ни стаа! Грешка!")


"НОВ КЛАС ГРЕШКА"
# class No_enough_BEER():
#     pass
# b = 0
# if b == 0:
#     raise No_enough_BEER()


"ЗА НЯКОЛКО ВИДА ГРЕШКИ TRY EXEPT"      # влиза в except ако грешката се случи в кода м/у try и except
while True:
    try:
        x = int(input("Pleace, enter a number 1: "))
        y = int(input("Pleace, enter a number 2: "))
        print(x/y)
        break

    # except ValueError:
    #     print("Oops! That was no valid number. Try again...")
    # except ZeroDivisionError:
    #     print("Oops! Second number can not be zero. Try again...")

    # или за по-кратко
    except (ValueError, ZeroDivisionError):
        print("Oops! Try again...")

    finally:
        print("Final clause")       # влиза в finaly след break и изпълнява преди да break-не