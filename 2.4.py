# 4.	Stwórz trzy nieduże słowniki o wartościach liczbowych
dict1 = {1: 2.8,
         2: 7,
         3: 12}

dict2 = {4: 56,
         5: 2.3,
         6: 11}

dict3 = {7: 7,
         8: 3.9,
         9: 0.2}

# a.	Napisz kod, który doda nowy element do jednego z nich
dict3.update({4: 209})
print(f'Updated dict3: {dict3}')

# b.	Napisz kod który połączy zawartość trzech słowników w jeden
dict123 = (dict1 | dict2 | dict3)
print(dict123)

# c.	Znajdź największą wartość całkowitą w słowniku
x = dict123.values()
print(x)
print(f'Max value from dictionaries: {max(x)}')

# d.	Znajdź sumę wszystkich wartości ze słownika
print(f'Sum of all items: {sum(x)}')
