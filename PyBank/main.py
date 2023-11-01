# import modules
import os
import csv

# set path, open file, and loop through columns
budget_data_csv = os.path.join("Resources/budget_data.csv")
with open (budget_data_csv, 'r') as budgetcsv:
    csv_reader = csv.reader(budgetcsv)
    header = next (csv_reader)
    print (header[0])
    for row in csv_reader:
        counter += int(row [1])
        Date = row [0]
        print (Date)
        print (counter)
print (counter)
