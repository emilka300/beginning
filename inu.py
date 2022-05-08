
def parzyste():
    liczba = 0
    while True:
        yield liczba
        liczba += 2


a = parzyste()
b = parzyste()

for i in a:
    print(i)
    if i >= 4:
        break

print(next(b))
print(next(a))
