# 2.	Za pomocą list oraz czterech funkcji zaimplementuj jednowymiarowy automat komórkowy w jego najprostszej wersji.
# https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
# _____________ Pierwsza będzie odpowiedzialna za inicjowanie uładu,
print("*******************************************************************")
print("Hello, this is Elementary Cellular Automaton created by Emilia Wach")
length = int(input("Initiate the array by inserting number of cells per line "))
length = length


# tutaj można też jakiś generatur wartości binarnej liczby dziesiętnego układu, ale lepiej zacząć od gotowej listy
# ruleset = [0, 1, 1, 1, 0, 1, 1, 0]  # rule 110
ruleset = [0, 1, 0, 1, 1, 0, 1, 0]  # rule 90
# ruleset = [1, 1, 0, 1, 1, 1, 1, 0]  # rule 222
# ruleset = [0, 1, 1, 1, 1, 1, 0, 1]  # rule 190
# ruleset = [0, 1, 1, 1, 1, 0, 0, 0]  # rule 30
# ruleset = [0, 1, 0, 1, 1, 0, 1, 0]  # rule 90
cd = []
cells = []


def inserting(leng):
    j = 0
    mid = leng % 2
    # jeśli ktoś będzie chcieć parzystą ilość komórek
    if mid == 0:
        for i in range(0, leng):
            if i == (leng/2) - 1:
                cells.append(1)
            elif i == leng/2:
                cells.append(1)
            else:
                cells.append(0)

    # jeśli ktoś będzie chcieć NIEparzystą ilość komórek
    else:
        for i in range(0, leng):
            if i == (leng / 2) - 0.5:
                cells.append(1)
            else:
                cells.append(0)

    return cells


cells = inserting(length)
cd.append(cells)
print(cd)
print(f'First line: {cells}')


# _____________ druga za aktualizację komórek,

def rules(a, b, c):
    if a == 1 and b == 1 and c == 1:
        print(f'Ruleset value: {ruleset[0]}')
        return ruleset[0]
    elif a == 1 and b == 1 and c == 0:
        print(f'Ruleset value: {ruleset[1]}')
        return ruleset[1]
    elif a == 1 and b == 0 and c == 1:
        print(f'Ruleset value: {ruleset[2]}')
        return ruleset[2]
    elif a == 1 and b == 0 and c == 0:
        print(f'Ruleset value: {ruleset[3]}')
        return ruleset[3]
    elif a == 0 and b == 1 and c == 1:
        print(f'Ruleset value: {ruleset[4]}')
        return ruleset[4]
    elif a == 0 and b == 1 and c == 0:
        print(f'Ruleset value: {ruleset[5]}')
        return ruleset[5]
    elif a == 0 and b == 0 and c == 1:
        print(f'Ruleset value: {ruleset[6]}')
        return ruleset[6]
    elif a == 0 and b == 0 and c == 0:
        print(f'Ruleset value: {ruleset[7]}')
        return ruleset[7]
    else:
        return 0


# _____________ trzecia wierszy,
nextgen = []
print(f'Cells 0: {cells[0]}')
print(f'Cells -1: {cells[-1]}')


def generate(cel, leng):
    for i in range(0, leng):
        print("i:", i)
        if i == leng - 1:
            right = int(cel[0])
        else:
            right = int(cel[i + 1])
        left = int(cel[i - 1])
        middle = int(cel[i])
        print(left, middle, right)
        nextgen.append(rules(left, middle, right))
    return nextgen


for g in range(1, 30):
    nextgen = generate(cells, length)
    print(f'Next generation: {nextgen}')
    cd.append(nextgen)
    cells = nextgen
    nextgen = []

# _____________ a czwarta za drukowanie wyników na ekranie.

for row in cd:
    for elem in row:
        print(elem, end=' ')
    print()

# print(ruleset[2])
