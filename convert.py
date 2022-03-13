import csv
import json

dataset = []
with open('dataset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dataset.append(row)

with open('dataset.json', 'w') as outfile:
    json.dump(dataset, outfile)