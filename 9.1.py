import numpy as np
import random
# 1.	Stwórz listę list, o losowych elementach liczbowych. List powinno być 10, a każda z nich powinna mieć 6 elementów.
# a.	Przekształć ją do postaci tablicy numpy

B = []
for i in range(0, 10):
    C = []
    for j in range(0, 6):
        C.append(random.randint(0, 100))
    B.append(C)

print(f'B: {B}')

A_new = np.array(B)
print(f'A_new: {A_new}')


A = np.round(100 * np.random.rand(10, 6))
print(f'A: {A}')


# b.	Za pomocą numpy policz sumę, średnią i odchylenie standardowe zbioru elementów
print(f'Sum:{np.sum(A, axis=0)}')
print(f'Mean:{np.mean(A, axis=0)}')
print(f'Std:{np.std(A, axis=0)}')