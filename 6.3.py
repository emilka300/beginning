# 3.	Stwórz kilka klas dziedziczących z klasy Człowiek. Przykładowo mogą to być:
# Chłopak, Dziewczyna, Student, Dziecko, Żołnierz, Piekarz itp.
# Klasy te powinny mieć swoje dodatkowe metody i pola zgodne ze specjalnością.
# Tutaj również mile widziana kreatywność.
# Spróbuj te klasy pochodne skonstuować tak, żeby niektóre z ich nadpisywały oryginalne
# metody klasy Człowiek. Stwórz po kilka obiektów tych klas spochodnych.

class Human:

    def __init__(self, name, last, age):
        # poniżej mam pola
        self.name = name  # pole
        self.last = last
        self.age = age
        self.energy = 100
        print(f'Information about: ', self.fullname(), f', age: {age}.')

    def fullname(self):
        return '{} {}'.format(self.name, self.last)

    def breathing(self, time):
        self.energy = self.energy - 1 * time
        print(f'After {time}h of breathing - Amount of energy: {self.energy}.')

    def drinking(self, liter):
        self.energy = self.energy + liter
        print(f'After drinking {liter}liters - Amount of energy: {self.energy}.')

    def eating(self, food, kcl):
        self.energy = self.energy + kcl
        print(f'After eating {food} - Amount of energy: {self.energy}.')

    def walking(self, distance):
        self.energy = self.energy - 5 * distance
        print(f'After {distance}km of walking - Amount of energy: {self.energy}.')

    def watching(self, time):
        self.energy = self.energy - 1 * time
        print(f'After {time}h of watching - Amount of energy: {self.energy}.')


class Student(Human):
    def __init__(self, name, last, age, stud_type):
        super().__init__(name, last, age)
        self.stud_type = stud_type
        print(f"Hi, I am a student. I study {stud_type}.")

    def __repr__(self):
        return str(self.__dict__)

    def studying(self, time):
        self.energy = self.energy - 1 * time
        print(f'After {time}h of studying - Amount of energy: {self.energy}.')

    def eating(self, food, kcl):
        super().eating(food, kcl - 10)
        print(f'Students need more food so energy level is lover then in older person.')


class Baby(Human):
    def __init__(self, name, last, age):
        super().__init__(name, last, age)
        print("Hi, I am a baby.")

    def walking(self, distance):
        if self.age < 2:
            print("I am too baby and I can't walk yet.")
        else:
            super().walking(distance)


class Cook(Human):
    def __init__(self, name, last, age):
        super(Cook, self).__init__(name, last, age)
        print("Hi, I am a cook.")


class Lecturer(Human):
    def __init__(self, name, last, age, students=None):
        super().__init__(name, last, age)
        print("Hi, I am a lecturer.")
        if students is None:
            self.students = []
        else:
            self.students = students

    def print_stud(self):
        print(f'these are {self.name} students: ')
        for s in self.students:
            print('--->', s.fullname())

    def add_stud(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    def remove_stud(self, stud):
        if stud in self.students:
            self.students.remove(stud)


print('--------------------------------------')
Emilia = Student("Emilia", "Wach", 24, "Management Engineering")
Emilia.drinking(2)
Emilia.studying(45)
Emilia.eating("burger", 400)
print('-------------next person--------------')
Stefcia = Baby("Stefcia", "Pert", 1)
Stefcia.walking(5)
print('-------------next person--------------')
Ignacy = Baby("Ignacy", "Robert", 5)
Ignacy.walking(5)
print('-------------next person--------------')
Szczepan = Cook("Szczepan", "Trylo", 25)
print('-------------next person--------------')
Krzysztof = Lecturer("Krzysztof", "Popiński", 51, [Emilia, Stefcia])
Krzysztof.print_stud()
Krzysztof.remove_stud(Stefcia)
Krzysztof.add_stud(Szczepan)
Krzysztof.print_stud()
