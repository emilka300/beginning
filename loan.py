# import math

# get the loan details per 1 month

money_owed = float(input("How much money do you owe, in dollars? "))
apr = float(input("What is the annual percentage rate? "))  # annual - coroczny
payment = float(input("What will your monthly payment be in dollars? "))
months = int(input("How many months calculate? "))
already_paid = float(0)
# monthly % rate divided by 100 to make it a %, then divided by 12 to make monthly
monthly_rate = apr / 100 / 12

for x in range(months):
    # add an interest - monthly playment for owning
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    y = money_owed - payment
    # end of loan
    if y < 0:
        print("That is the last payment is", payment + y)
        print("You paid off the loan in", x + 1, "months")
        break

    # loan after paying off
    money_owed = money_owed - payment

    # how much you already paid
    if x > 1:
        already_paid += payment

# print the result after this month
print("Paid", payment, "of which", interest_paid, "was interest. You have already paid: ", already_paid, ".", end=" ")
print("Now you owe", round(money_owed, 2))
