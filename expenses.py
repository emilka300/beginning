
expenses = [10.5, 8, 5, 15, 20, 5, 3]
sume = 0

for expense in expenses:
    sume += expense

# total = sum(expenses) -> faster way!

print("You spent $", sume, " on lunch this week.", sep='')  # sep - specifies the separator in comma place


# other way

expenses = []
num_expenses = int(input("Enter # of expenses:\n"))
for i in range(num_expenses):
    expenses.append(float(input("Enter and expense:")))

print(expenses)
total = sum(expenses)

print("You spent $", total, sep='')




