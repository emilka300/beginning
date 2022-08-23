import time
# 1.	Używając pętli for stwórz słownik w którym kluczami będą
# liczby całkowite od 1 do 100, a wartościami kwadraty tych liczb.
dict0 = {}
for i in range(101):
    dict0.update({i: i ** 2})

print(dict0)

# 2.	Stwórz dwie zagnieżdżone pętle, które robią coś, na przykład dodają jakiś element do listy.
# Najpierw zewnętrzna będzie miała długość 10000 przebiegów, a wewnętrzna 100, a później odwrotnie.
# Przy użyciu biblioteki time porównaj prędkość działania obu wariantów.
# Który z nich będzie korzystniejszy?
lista = []
lista2 = []
start = time.time()

for i in range(10001):
    for j in range(101):
        lista.append(i + j)

end = time.time()
print(f'Time needed for loops to be done: {end - start} variant 10000, 100')

start2 = time.time()

for k in range(101):
    for l in range(10001):
        lista2.append(k + l)

end2 = time.time()
print(f'Time needed for loops to be done: {end2 - start2} variant 100, 100000')

if end - start > end2 - start2:
    print("Second variant is more efficient.")
else:
    print("First variant is more efficient.")
