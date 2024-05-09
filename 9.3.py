# 3.	Wykorzystując wbudowane funkcje pakietu numpy stwórz losową tablicę 60x15. Przyjmując, że reprezentuje
# ona  60 punktów w 15 wymiarowej przestrzeni, policz:
# a.	Odległość euklidesową każego punktu od początku układu współrzędnych -> p = 0
import numpy as np

A = np.round(100 * np.random.rand(15, 60), decimals=1)
print(f'A: {A}')
# Euk = np.sqrt((q-p)**2 + (q-p)**2)

for i in range(0, 60):
    S = 0
    for j in range(0, 15):
        S = S + (A[j, i]) ** 2
    E = np.sqrt(S)
    print(f'Point {i}. Distance from the beginning : {E}.')
# b.	Odległość euklidesową między każdą parą punktów. W tym celu stwórz funkcję.
# Czy potrafisz to zrobić w jednej linijce?

for i in range(0, 60):
    S = 0  # A[0,0]
    k = 0  # A[0,0]
    while k <= 59:
        for j in range(0, 15):
            S = S + (A[j, i] - A[j, k]) ** 2
        E = np.sqrt(S)
        S = 0
        print(f'Point {i}, and {k}. Distance from each other : {E}.')
        k += 1

for i, j, k in range(0, 60), range(0, 15), range(0, 60): print(np.sqrt(sum(A[j, i] - A[j, k]) ** 2))
