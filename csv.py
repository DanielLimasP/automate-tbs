import csv
from pathlib import Path

# Makes it easier
cwd = Path.cwd() / csv
cwd = Path.cwd() / 'csv'

example_file = open(cwd / 'example.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
example_data

exampleFile = open(cwd / 'example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

outputFile = open(cwd / 'output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

exampleFile = open('example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name',    'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

outputFile = open(cwd / 'output_with_headers.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})

outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})

outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

outputFile.close()