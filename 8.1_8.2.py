import pandas as pd
import csv
# 1.	Stworzyć klasę , która będzie odczytywała zapisane pliki i odtwarzała zawarte w nich obiekty


class Reading:

    def __init__(self, name):
        self.name = ""
        self.rows = []
        self.cols = []
        self.df = {}
        self.json_file = {}

    def read_csv(self, name):
        print('CSV reading: ...')
        try:
            self.name = name
            with open(name, 'r') as csv_file:
                reader = csv.reader(csv_file)
                self.cols = csv_file.readline()
                for line in reader:
                    self.rows.append(line)
            print(f'\rCols: {self.cols} \rRows: {self.rows}')
        except Exception as e:
            print(f'Error message: {repr(e)}')

    def read_csv_df(self, name):
        print("Pandas reading: ...")
        try:
            self.name = name
            self.df = pd.read_csv(self.name)
            print(self.df.head())
            del self.df['Unnamed: 0']
            print(f'After deletion: \r{self.df.head()}')
        except Exception as e:
            print(f'Error message: {repr(e)}')

    def read_json(self, name):
        print("JSON reading: ...")
        try:
            self.name = name
            self.json_file = pd.read_json(name)
            print(self.json_file)
        except Exception as e:
            print(f'Error message: {repr(e)}')


Action = Reading(None)
Action.read_csv("data_classic.csv")
print("---------------------------------------------")
Action.read_csv_df('data_df.csv')
print("---------------------------------------------")
Action.read_json("data.json")
print("---------------------------------------------")