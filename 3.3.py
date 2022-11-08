# 3.	Przy użyciu pętli oraz wyrażeń warunkowych znajdź wszystkie
# liczby pierwsze mniejsze od 10000
# Liczba pierwsza:
# - liczba naturalne n > 1, i - int(i) == 0
# - dwa dzielniki naturalne: 1 oraz n.

l_pierwsza = []
l_zlozona = []

for i in range(2, 10001):
    for j in range(2, 10001):
        if i % j == 0 and i != j:
            l_zlozona.append(i)
            break
    if i not in l_zlozona:
        l_pierwsza.append(i)


print(f'Prime numbers in range (1 - 10001> are: {l_pierwsza}\nzlozone: {l_zlozona}')
