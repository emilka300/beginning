# 1.	Stwórz miniaturową bazę danych, złożoną z jednej pseudotabeli.
# Każdy wpis w bazie powinien być słownikiem, a kolejne wpisy powinny być przechowywane w liście.
# a.	Pojedynczy wpis powinien zawierać: imię, nazwisko, wiek, płeć, dochody,
# majątek, liczbę dzieci, wykształcenie (podstawowe, średnie, studia: 1, 2, 3 stopnia),
# wielkość miejsca zamieszkania (1-100 mieszkańców, 101-1000, 1001-10000, 10001-100000,
# 100001-1000000, powyżej 1000000)
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
new = {}
for i in range(1, 21):
    new = {"name": random.choice(name),
           "surname": random.choice(surname),
           "age": random.randint(18, 99),
           "sex": random.choice(sex),
           "income": random.randint(0, 100000),
           "property": random.randint(0, 10000000),
           "children": random.choice(children),
           "education": random.choice(education),
           "citizens": random.choice(citizens)}
    database.append(new)

print(database)

# c.	Za pomocą pętli i instrukcji warunkowych przeszukaj bazę i każ jej zwrócić
# wszystkich mieszkańców spełniających określone kryteria, na przykład o dochodach
# powyżej jakiegoś progu, lub miejscu zamieszkania poniżej jakiegoś limitu.
print("One condition results:")
for x in database:
    if x["income"] > 50000:
        print(x["name"], x["surname"])

# d.	Teraz zwróć mieszkańców spełniających oba kryteria naraz.
print("Two conditions results:")
for x in database:
    if x["income"] > 50000 and x["education"] == "first-degree studies":
        print(x["name"], x["surname"])


# e.	Posortuj tabelę alfabetycznie, po nazwiskach

def sortFunction(value):
    return value["surname"]


sortedDatabase = sorted(database, key=sortFunction)
print(sortedDatabase)
