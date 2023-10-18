import csv

clean_dataset = []

with open('dataset.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        if None not in row and '' not in row and row not in clean_dataset:
            clean_dataset.append(row)

print(clean_dataset)
