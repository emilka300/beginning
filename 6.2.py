# 2.	Stwórz nadrzędną klasę Człowiek, zawierającą metody:
# oddychanie, picie, jedzenie, chodzenie, patrzenie, oraz pola: imię i energia”.
# Pól i metod może być więcej.
# Każda z tych metod po wywołaniu powinna wyświetlać jakiś komunikat za pomocą instrukcji print(),
# niektóre metody mogą przyjmować wartości.
#
# Na przykład wywołanie jedzenie(‘jabłko’) wyswietli komunikat: ‘mmmm jakie pyszne jabłko’,
# może również zwiększyć wewnętrzny poziom energii. Analogicznie chodzenie zużyje energię.
# Liczę na kreatywność i dowcip. Stwórz kilka obiektów klasy człowiek, różniących się imieniem, energią itp.


class Human:

    def __init__(self, name, age):
        # poniżej mam pola
        self.name = name #pole
        self.age = age
        self.energy = 100
        print(f'Information about {name}: age: {age}.')

    def __repr__(self):
        return str(self.__dict__)

    def breathing(self, time):
        self.energy = self.energy - 1 * time
        print(f'After {time}h of breathing - Amount of energy: {self.energy}.')

    def drinking(self, liter):
        self.energy = self.energy + liter
        print(f'After drinking {liter} liters - Amount of energy: {self.energy}.')

    def eating(self, food, kcl):
        self.energy = self.energy + kcl
        print(f'After eating {food} - Amount of energy: {self.energy}.')

    def walking(self, distance):
        self.energy = self.energy - 5 * distance
        print(f'After {distance}km of walking - Amount of energy: {self.energy}.')

    def watching(self, time):
        self.energy = self.energy - 1 * time
        print(f'After {time}h of watching - Amount of energy: {self.energy}.')

# tu tworze różne obiekty
Agnieszka = Human("Agnieszka", 21)
Agnieszka.breathing(2)
Agnieszka.eating('banana', 200)
Agnieszka.drinking(9)

Filip = Human("Filip", 22)
Filip.breathing(10)

print(Agnieszka)
print(Filip)


def y():
    print('xxxxxx')

class A:

    def __init__(self):
        self.wiek = 10
        self.imie = 1

    def x(self):
        print('aaa', self.imie)

# reprezentacja - tutaj tworzymy słownik

    def __repr__(self):
        return str(self.__dict__)


class B(A):

    def __init__(self):
        super().__init__()
        self.wzrost = 5

    def x(self):
        super().x()
        print('dodatkowe działanie', self.wiek, self.wzrost)

    def __eq__(self, other):
        return self.wzrost == other.wzrost


a = A()
a.aaaa = 1 # tutaj moemy dodać sobie dodatkowy argument do obiektu
b1 = B()
b2 = B()
b2.wzrost = 10

a.x()
b1.x()
print("a: ", a)
print("b1: ", b1)
print(b1 == b2)
print(b1.wzrost == b2.wzrost)

