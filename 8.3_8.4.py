# 3.	Stworzyc funkcję liczącą silnię, może być rekurencyjnie, może być iteracyjnie. Funkcja
# powinna pytać użytkownika o podanie n i wyrzucać n!. W przypadku n < 0 funkcja zwraca wyjątek informując o błędzie.

def factorial():
    print("")
    print('\x1b[4;30;43m' + " This is a factorial machine. " + '\x1b[0m')
    value = int(input("Choose base of factorial you want to know. "))
    value_1 = value
    value_2 = value
    result = None
    if value > 1:
        while value_2 > 1:
            result = value_1 * (value_2 - 1)
            value_1 = result
            value_2 -= 1
            print(value_2)
    elif value == 1:
        result = 1
    else:
        return 0

    print('\x1b[7;30;45m' + f" Factorial of {value} is equal to: {result} " + '\x1b[0m')
    answer = input("Do you want to continue? Y/N ")
    answer = answer.upper()
    if answer == "Y":
        print("---------------------------------------")
        factorial_func()
    elif answer == "N":
        print("Goodbye.")
        print("---------------------------------------")
    else:
        print("You chose wrong answer. Default respond has been chosen. Program stopped.")


def factorial_func():
    if factorial() == 0:
        print("You chose wrong number. Try again.")
        print("Reloading...")
        factorial_func()


factorial_func()
