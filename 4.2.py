# 2.	Pozamykaj stworzony kod w funkcje. Pierwsza funkcja powinna przyjmować jako
# argument liczbę wierszy i tworzyć tabelę.
import random

name = ["Katarzyna", "Joanna", "Paweł", "Krzysztof"]
surname = ["Wilk", "Lok", "Bach", "Stos"]
sex = ["female", "male", "non-binary"]
children = [0, 1, 2, 3, 4, 5, 6, 7]
education = ["primary education", "secondary education", "first-degree studies", "second-degree studies",
             "third-degree studies"]
citizens = ["1-100", "101-1000", "1001-10000", "10001-100000", "100001-1000000", "> 1000000"]
database = [
    {"name": "Emilia",
     "surname": "Wach",
     "age": 23,
     "sex": "female",
     "income": 8500,
     "property": 10000,
     "children": 0,
     "education": "first-degree studies",
     "citizens": "100001 - 1000000"}
]

# b.	Wygeneruj losowo bazę danych zawierającą 200 lub więcej takiech wpisów (przechowywanych w liście)
verse = int(input("Write how many records you want: "))


def table(rows, na, sur, se, chil, ed, cit):
    for i in range(1, rows):
        new = {"name": random.choice(na),
               "surname": random.choice(sur),
               "age": random.randint(18, 99),
               "sex": random.choice(se),
               "income": random.randint(0, 100000),
               "property": random.randint(0, 10000000),
               "children": random.choice(chil),
               "education": random.choice(ed),
               "citizens": random.choice(cit)}
        database.append(new)
    return database


table(verse, name, surname, sex, children, education, citizens)
print(database)

# Druga funkcja powinna przeszukiwać tabelę, którą przyjmie jako jeden z argumentów.

# c.	Za pomocą pętli i instrukcji warunkowych przeszukaj bazę i każ jej zwrócić
# wszystkich mieszkańców spełniających określone kryteria, na przykład o dochodach
# powyżej jakiegoś progu, lub miejscu zamieszkania poniżej jakiegoś limitu.
condition = input("Choose parameter form list: (name, surname, age, sex, income, \
property, children, education, citizens) ")


def condition_biggerthen(con, val):
    for y in database:
        if y[con] > val:
            print(y["name"], y["surname"])


def condition_lowerthen(con, val):
    for y in database:
        if y[con] < val:
            print(y["name"], y["surname"])


def condition_equal(con, val):
    for y in database:
        if y[con] == val:
            print(y["name"], y["surname"])


if condition == "name" or condition == "surname" or condition == "sex" or condition == "children" \
        or condition == "education" or condition == "citizens":
    if condition == "name":
        value = input("Choose name from list: (Katarzyna, Joanna, Paweł, Krzysztof) ")
        print("One condition results:")
        condition_equal(condition, value)
    elif condition == "surname":
        value = input("Choose surname from list: (Wilk, Lok, Bach, Stos) ")
        print("One condition results:")
        condition_equal(condition, value)
    elif condition == "sex":
        value = input('Choose sex from list: (female, male, non-binary) ')
        print("One condition results: ")
        condition_equal(condition, value)
    elif condition == "children":
        value = int(input("Choose number of children from list: (0, 1, 2, 3, 4, 5, 6, 7) "))
        print("One condition results: ")
        condition_equal(condition, value)
    elif condition == "education":
        value = input("Choose education level from list: (primary education, secondary education,\
first-degree studies, second-degree studies, third-degree studies) ")
        print("One condition results:")
        condition_equal(condition, value)
    else:
        value = input("Choose amount of citizens from list: (1-100, 101-1000, 1001-10000,\
10001-100000, 100001-1000000, > 1000000) ")
        print("One condition results:")
        condition_equal(condition, value)
else:
    value = int(input("Input numerical values: "))
    types = input("Choose type of sign form list: (> , <, ==) ")
    print("One condition results: ")
    if types == ">":
        condition_biggerthen(condition, value)
    elif types == "<":
        condition_lowerthen(condition, value)
    else:
        condition_equal(condition, value)


# d.	Teraz zwróć mieszkańców spełniających oba kryteria naraz.
print("Two conditions results:")
for x in database:
    if x["income"] > 50000 and x["education"] == "first-degree studies":
        print(x["name"], x["surname"])


# e.	Posortuj tabelę alfabetycznie, po nazwiskach

def sortFunction(value):
    return value["surname"]


sortedDatabase = sorted(database, key=sortFunction)
print(f'Sorted database:{sortedDatabase}')
