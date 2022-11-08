# 3.	Stwórz listę zawierającą liczby. Niemniej, niż 25 liczb, powinno też znajdować się kilka duplikatów
lista = [24, 3, 3, 78, 109, 25, 11, 340, 660, 666, 666, 45, 33, 45, 22, 89, 100, 207, 345, 7, 3, 22, 56, 7003, 1]
print(len(lista))

# a.	Wyświetl największy i najmniejszy element listy
print(f' Maximum value: {max(lista)} \n Minimum value: {min(lista)}')

# b.	Wyświetl sumę elementów listy
suma = sum(lista)

# longer version
# suma = 0
# for i in lista:
#     suma = suma + i

print(f' Sum = {suma}')

# c.	Uporządkuj listę rosnąco i malejąco
# https://docs.python.org/3/howto/sorting.html#ascending-and-descending <- w razie gdybym potrzebowała ciekawiej
sorted_ascending = sorted(lista)
# both options are valid
sorted_descending_v1 = sorted(lista, reverse=True)
sorted_descending_v2 = sorted_ascending[::-1]
print(f' List ascending sorted: {sorted_ascending}\nList descending sorted {sorted_descending_v1, sorted_descending_v2}')

# d.	Wyświetl trzy najmniejsze i trzy największe liczby
print(f' Three numbers from the beginning (ascended list): {sorted_ascending[0:3]} \n Three numbers from the end\
{sorted_ascending[-3:]}')
print(f' Three numbers from the beginning (descended list): {sorted_descending_v1[0:3]} \n Three numbers from the end\
{sorted_descending_v1[-3:]}')

# e.	Usuń duplikaty

noduplicats = set(lista)
print(noduplicats)
print(len(noduplicats))

