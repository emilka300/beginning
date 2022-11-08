# 1.	Stwórz dwie funkcje, jedna z nich wygeneruje osowo listę liczb o zadanej długości
# Druga tę listę posortuje używając metody sortowania bąbelkowego


import random
random_list = []
length = 0


def lista():
    length = int(input("Input number of randomly generated list. "))

    for i in range(0, length):
        new = random.randint(0, 99)
        random_list.append(new)

    return random_list, length


def bombelki(lists, lengt):
    k = 1
    while k == 1:
        k = 0
        for i in range(0, lengt):
            j = i + 1
            print("j = ", j)
            if j == lengt:
                print(k)
                break
            else:
                a = random_list[i]
                print("a = ", a)
                b = random_list[j]
                print("b = ", b)
                if a > b:
                    random_list[i] = b
                    random_list[j] = a
                    k = 1
    print(random_list)


lista()
leng = len(random_list)
print(random_list, leng)

bombelki(random_list, leng)
