# pip install pandas in terminal
import random
import pandas as pd
import csv
import json
from abc import ABC, abstractmethod


# Zad 3. Proszę stworzyc klase abstrakyjną / interfejs dla wyżej napisanych klas
# tworzymy szablon matod, które muszą wystąpić w podklasie klasy Save_file (daje to pewność, ze o niczym \
# nie zapomnieliśmy)
class SaveFile(ABC):
    @abstractmethod
    def save_csv(self):
        pass

    @abstractmethod
    def save_csv_df(self):
        pass

    @abstractmethod
    def save_json(self):
        pass


# to save export data to csv I can save data using csv packege OR pandas (DataFrame)
class Save(SaveFile):

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.g_list = []
        self.d = {}

    def save_csv(self):
        with open("data_classic.csv", "w", newline='') as f:
            write = csv.writer(f)
            write.writerow(self.cols)
            write.writerows(self.rows)
        print("CSV saved")

    def save_csv_df(self):
        df = pd.DataFrame(self.rows, columns=self.cols, dtype=float)
        print(df)
        df.to_csv('data_df.csv')
        print("CSV saved using DataFrame")

    # Zad 2.  Prosze napisac klase ktora bedzie zapisywać dane zgromadzone w "data" w pliku w formacie JSON
    # https://pl.wikipedia.org/wiki/JSON

    def save_json(self):
        for value in self.rows:
            i = 0
            self.d = {}
            for name in self.cols:
                if i <= 5:
                    self.d[str(name)] = value[i]
                    # print(i)
                    # print(f'{name}: {value[i]}')
                    # print(self.d)
                    i = i + 1
            self.g_list.append(self.d)
            # print("---------------------------------------------")
        print(self.g_list)
        json_string = json.dumps(self.g_list)
        print(json_string)
        json_file = open("data.json", "w")
        json_file.write(json_string)
        json_file.close()
        print("Json saved")


n0 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum justo sem, venenatis eget elementum ut, \
pulvinar rutrum diam. Suspendisse ut semper diam, in fringilla lectus. Mauris semper mi at ornare tincidunt. \
Phasellus ac diam volutpat, pretium neque in, tempor odio. Donec ullamcorper sapien ac pretium mattis. Suspendisse \
quis mollis dui."
n1 = n0.replace(',', "")
n2 = n1.replace('.', "")
n3 = n2.split(" ")

names = []
columns = ["name", "surname", "income", "street", "home number", "phone number"]

for n in n3:
    names.append(n.capitalize())

data = []

for _ in range(1, 1000):
    data.append([
        random.choice(names),  # imie
        random.choice(names),  # nazisko
        random.uniform(1200, 100000),  # zarobiki
        random.choice(names),  # nazwa ulicy
        random.randint(1, 30),  # numer domu
        random.randint(1000000, 3000000)  # numer telefonu
    ])
# print(data)
Data = Save(data, columns)
# Data.save_csv()
# print("---------------------------------------------")
# Data.save_csv_df()
# print("---------------------------------------------")
Data.save_json()
print("---------------------------------------------")
