import numpy as np
import random
# 2.	Wykorzystując wbudowane funkcje pakietu numpy stwórz losową tablicę 20x50. Wykorzystując wbudowane fnkcje numpy
# a.	Policz średnią wyrazów tablicy
A = np.round(100 * np.random.rand(20, 50))
print(f'A: {A}')
print(f'Mean: {np.mean(A)}')
B = np.empty((20, 50), dtype=float)
B = np.round(B, decimals=1)
# print(f'B: {B}')
C = np.random.randint(2, 100, (20, 50))
# print(f'C: {C}')
# b.	Policz średnie każdego wiersza i przedstaw w postaci tablicy (wektora)
print(f'Verses mean value: {np.mean(A, axis=1)}')

# c.	Policz średnie każdej kolumny i przedstaw w postaci tablicy (wektora)
print(f'Columns mean value: {np.mean(A, axis=0)}')

# d.	Zamień wiersze z kolumnami (transponuj)
trans_A = A.T
print(f'Transposed A: {trans_A}')

# e.	Pomnóż tablicę przez 5.5
print(f'Multiplied by 5: {A*5}')

# f.	Policz tablicę, której każdy wyraz będzie trzecią potęgą oryginalnej tablicy
print(f'A to the power of 3: {A**3}')
print(A[19, 49]**3)
