menu = {"breakfast": ['Egg Sandwich', 'Bagel', 'Coffee'],
        "lunch": ['BLT', 'PB&J', 'Turkey Sandwich'],
        "dinner": ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print("In today menus we can offer you: ")
for i in menu:
    print(i)

offer = input("Does something interested you? ").strip().lower()

# printing dishes in chosen part of menu
for x in menu[offer]:
    print(x)

# second version (all dishes)
print("------------all dishes---------------")
for x in menu:
    for xx in menu[x]:
        print(xx)

# just a menu
print("-----------just a menu----------------")
for k, e in menu.items():
    print(k, e)