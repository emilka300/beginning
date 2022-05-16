# import math

# get the loan details per 1 month

name = input("What's your name? ").strip().title()
money_owed = float(input("How much money do you owe, in dollars? "))
apr = float(input("What is the annual percentage rate? "))  # annual - coroczny
payment: float = float(input("What will your monthly payment be in dollars? "))
# months = int(input("How many months calculate? "))
already_paid = float(0)
# monthly % rate divided by 100 to make it a %, then divided by 12 to make monthly
monthly_rate = float(apr / 100 / 12)
m = 0
y = float(1)
x = int(0)
interest_paid = float(0)
loan = money_owed

while y > 0:
    # add an interest - monthly playment for owning
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    y = money_owed - payment
    # loan after paying off
    money_owed = money_owed - payment
    m += 1
    # how much you already paid
    x += 1
    if x > 1:
        already_paid += payment
else:
    print(f"After {m} months your loan will be payed off.")
    print("----------------------------------------------")

# print the result after this month
print("Paid", payment, "of which", interest_paid, "was interest. You have already paid: ", already_paid, ".", end=" ")
print("Now you owe", round(money_owed, 2))

# list with all data
list = ['name: ', name, '\n',
        'loan value: ', str(loan), '\n',
        'annual percentage rate: ', f'{apr}', '\n',
        'payment: ', str(payment), '\n',
        'full payment: ', str(already_paid), '\n', '\n']

with open("zapis.txt", 'a') as file:
    file.writelines(list)
