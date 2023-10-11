# import the modules
import os
import csv

# set the path for the csv
os.path.join("/Users/yenori/Desktop/GitHub/python-challenge/PyPoll/Resources")

# set the variables

# open the csv
with open ('election_data.csv') as csvfile:
    csvreader = csv.dictReader(csvfile)

# Calculate the total number of votes cast:


