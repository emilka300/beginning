# 3.	ZADANIE DLA CHĘTNYCH
# Analogicznie jak w poprzednich zadaniach stwórz miniaturową bazę danych,
# Jednak tym razem będzie się składała z dwóch tabel.
# W pierwszej wpisy powinny być mieć podobną strukturę,
# tylko zamiast wielkości miejsca zamieszkania powinna być nazwa miejscowości.
# Druga tabela powinna zawierać wpisy z: nazwą miejscowości, liczbą mieszkańców,
# listą atrakcji turystycznych.
# Zapytanie do takiej bazy powinno zwracać wpisy będące połączeniem dwóch tabel.
# To znaczy informacje o obywatelu, nazwę miejscowości i wszystkie informacje o tej miejscowości
# zawarte w drugiej tabeli. Taka operacja jest podobna do dizałania komendy JOIN znanej z SQLa.

import random

name = ["Katarzyna", "Joanna", "Paweł", "Krzysztof"]
surname = ["Wilk", "Lok", "Bach", "Stos"]
sex = ["female", "male", "non-binary"]
children = [0, 1, 2, 3, 4, 5, 6, 7]
education = ["primary education", "secondary education", "first-degree studies", "second-degree studies",
             "third-degree studies"]
cities = ["Wrocław", "Warszawa", "Oława", "Radwanice", "Village", "Mini village"]
database = [
    {"name": "Emilia",
     "surname": "Wach",
     "age": 23,
     "sex": "female",
     "income": 8500,
     "property": 10000,
     "children": 0,
     "education": "first-degree studies",
     "cities": "Wrocław"}
]

city = [
    {"name": "Wrocław", "citizens": "100001-1000000", "attractions": 500},
    {"name": "Warszawa", "citizens": "> 1000000", "attractions": 1000},
    {"name": "Oława", "citizens": "10001-100000", "attractions": 200},
    {"name": "Radwanice", "citizens": "1001-10000", "attractions": 100},
    {"name": "Village", "citizens": "101-1000", "attractions": 50},
    {"name": "Mini village", "citizens": "1-100", "attractions": 10}
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
               "cities": random.choice(cit)}
        database.append(new)
    return database


table(verse, name, surname, sex, children, education, cities)
print(database)

# Druga funkcja powinna przeszukiwać tabelę, którą przyjmie jako jeden z argumentów.

# c.	Za pomocą pętli i instrukcji warunkowych przeszukaj bazę i każ jej zwrócić
# wszystkich mieszkańców spełniających określone kryteria, na przykład o dochodach
# powyżej jakiegoś progu, lub miejscu zamieszkania poniżej jakiegoś limitu.
condition = input("Choose parameter form list: (name, surname, age, sex, income, \
property, children, education, cities) ")


def condition_biggerthen(con, val):
    for y in database:
        if y[con] > val:
            for c in city:
                if c["name"] == y["cities"]:
                    print(y["name"], y["surname"], c["name"], c["citizens"], c["attractions"])


def condition_lowerthen(con, val):
    for y in database:
        if y[con] < val:
            for c in city:
                if c["name"] == y["cities"]:
                    print(y["name"], y["surname"], c["name"], c["citizens"], c["attractions"])


def condition_equal(con, val):
    for y in database:
        if y[con] == val:
            for c in city:
                if c["name"] == y["cities"]:
                    print(y["name"], y["surname"], c["name"], c["citizens"], c["attractions"])


if condition == "name" or condition == "surname" or condition == "sex" or condition == "children" \
        or condition == "education" or condition == "cities":
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
        value = input("Choose amount of citizens from list: (Wrocław, Warszawa, Oława, Radwanice, Village, \
Mini village) ")
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
