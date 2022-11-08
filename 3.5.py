import random
# 5.	Stwórz listę 2000 losowych liczb z przedziału od 1 do 100.
# Następnie „posortuj” jej zawartość używając czterech innych list,
# które mają zawierać wyłącznie: liczby parzyste, liczby podzielne przez 3,
# liczby podzielne przez 5, resztę.
original_list = []
parzyste = []
podzielneprzeztrzy = []
podzielneprzezpiec = []
other = []


for i in range(0, 2001):
    x = random.randint(0, 101)
    original_list.append(x)

# for i in original_list:
#     if i % 2 == 0:
#         parzyste.append(i)

parzyste = [x for x in original_list if x % 2 == 0]

# for i in original_list:
#     if i % 3 == 0:
#         podzielneprzeztrzy.append(i)

podzielneprzeztrzy = [x for x in original_list if x % 3 == 0]

# for i in original_list:
#     if i % 5 == 0:
#         podzielneprzezpiec.append(i)

podzielneprzezpiec = [x for x in original_list if x % 5 == 0]

other = [x for x in original_list if x not in parzyste and x not in podzielneprzeztrzy and x not in podzielneprzezpiec]

print(f'Even numbers from range 1 - 2000: {parzyste}\nNumbers divisible by three:{podzielneprzeztrzy}\nNumbers divisible by five:{podzielneprzezpiec}\nOther numbers:{other}')
