import csv


def write(data):
    with open('repositories.csv', "w",  newline='') as f:
        writer = csv.writer(f)
        for el in data:
            row = list(el.values())
            writer.writerow(row)

