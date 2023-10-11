# import the modules
import os
import csv

# set the path for the csv
budget_data_csv = os.path.join("/Users/yenori/Desktop/GitHub/python-challenge/PyBank/Resources")

# set the variables
total_months = 0
total_revenue = 0
revenue_of_change = 0
revenue_average = 0

# open the csv
with open ('budget_data.csv') as csvfile:
    csvreader = csv.dictReader(csvfile)


