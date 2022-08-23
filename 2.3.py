# 3.	Stwórz listę zawierającą liczby. Niemniej, niż 25 liczb, powinno też znajdować się kilka duplikatów
lista = [24, 3, 3, 78, 109, 25, 11, 340, 660, 666, 666, 45, 33, 45, 22, 89, 100, 207, 345, 7, 3, 22, 56, 7003, 1]
print(len(lista))

# a.	Wyświetl największy i najmniejszy element listy
print(f' Maximum value: {max(lista)} \n Minimum value: {min(lista)}')

# b.	Wyświetl sumę elementów listy
suma = 0

for i in lista:
    suma = suma + i

print(f' Sum = {suma}')

# c.	Uporządkuj listę rosnąco i malejąco
sorted = sorted(lista)
print(sorted)

# d.	Wyświetl trzy najmniejsze i trzy największe liczby
print(f' Three numbers from the beginning: {sorted[0:3]} \n Three numbers from the end {sorted[22: 25]}')

# e.	Usuń duplikaty

noduplicats = set(lista)
print(noduplicats)
print(len(noduplicats))

