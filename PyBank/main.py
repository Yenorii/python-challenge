# import the modules
import os
import csv

# set the path for the csv
budget_data_csv = os.path.join("/Users/yenori/Desktop/GitHub/python-challenge/PyBank/Resources")

# (?) set the variables (?)
total_months = 0

# open the csv
with open ('budget_data.csv') as csvfile:
    csvreader = csv.dictReader(csvfile)

    # loop throught the 'Date'row
    for row in csvreader:

        # TASK 1: Calculate the total number of months included in the dataset
        total_months += 1

        # TASK 2: Calculate the 


    

