# import the modules
import os
import csv

# set path and open csv
election_data_csv = os.path.join("/Users/yenori/Desktop/GitHub/python-challenge/PyPoll/Resources")
with open ('election_data.csv') as csvfile:
    csvreader = csv.dictReader(csvfile)

# run through the data

# variables:

# calculate the total number of votes cast:


