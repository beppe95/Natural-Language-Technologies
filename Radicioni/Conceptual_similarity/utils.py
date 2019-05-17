import csv


def read_csv_file(filepath: str):
    with open(filepath, encoding='utf-8') as file:
        reader = csv.reader(file, filter(lambda row: row!= '#', file), delimiter=' ', quotechar='|')

        i = 0
        for elem in reader:
            i += 1
            print(elem, i)