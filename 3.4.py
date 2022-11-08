import random

# 4.	Używając biblioteki random stwórz program dodający do listy
# losowe liczby całkowite z przedziału od 0 do 100, który jednak zatrzyma się
# gdy wylosuje liczbę 83. Wykonaj to ćwiczenie w dwóch wariantach,
# najpierw z użyciem pętli while, a następnie przy użyciu pętli for oraz polecenia break.

# 1 variant with while loop
x = 0
random_while = []
while x != 83:
    x = random.randint(0, 100)
    random_while.append(x)

print(random_while)

# 2 variant with for loop
random_for = []
n = 100
for i in iter(lambda: random.randint(0, 100), 83):
    x = random.randint(0, 100)
    random_for.append(x)
    n += 1
    if x == 83:
        break
print(random_for, n - 100, sep='\n')
