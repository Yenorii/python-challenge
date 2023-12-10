{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "34d4515f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "Diana DeGette: 73.812% (272892)\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "-------------------------\n",
      "Total Votes: 369711\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "# import modules\n",
    "import os\n",
    "import csv\n",
    "\n",
    "# Variables:\n",
    "total_votes = 0  # the total number of votes cast\n",
    "candidates = {}  # a dictionary to tally votes for each candidate\n",
    "\n",
    "# Prepare data\n",
    "election_data_csv = os.path.join(\"Resources/election_data.csv\")  # set file path\n",
    "with open(election_data_csv) as electioncsv:  # open file\n",
    "    csv_reader = csv.reader(electioncsv)  # loop through rows\n",
    "    header = next(csv_reader)  # skip header row\n",
    "    \n",
    "    # Loop through data and tally votes for each candidate\n",
    "    for row in csv_reader:\n",
    "        Voter_ID = row[0]  # grab voter IDs from column A\n",
    "        total_votes += 1  # increase by 1 for each voter ID to count the total votes\n",
    "        Candidate = row[2]  # grab candidates from column C\n",
    "        \n",
    "        # Tally votes for each candidate in the candidates dictionary\n",
    "        if Candidate in candidates:\n",
    "            candidates[Candidate] += 1  # increment the candidate's vote count by 1\n",
    "        else:\n",
    "            candidates[Candidate] = 1  # if new candidate, start count at 1\n",
    "            \n",
    "    # Find the winner    \n",
    "    max_votes = max(candidates.values())\n",
    "    winner = [candidate for candidate, votes in candidates.items() if votes == max_votes][0]\n",
    "\n",
    "    for candidate, votes in candidates.items():\n",
    "        percentage = (votes / total_votes) * 100\n",
    "\n",
    "# Calculate and print the analysis after tallying votes\n",
    "print(\"Election Results\")\n",
    "print(\"-------------------------\")\n",
    "for candidate, votes in candidates.items():\n",
    "    percentage = (votes / total_votes) * 100\n",
    "    print(f\"{candidate}: {percentage:.3f}% ({votes})\")\n",
    "print(\"-------------------------\")\n",
    "print(f\"Total Votes: {total_votes}\")\n",
    "print(\"-------------------------\")\n",
    "print(f\"Winner: {winner}\")\n",
    "print(\"-------------------------\")\n",
    "\n",
    "# Create a new text file\n",
    "output_file_path = os.path.join(\"analysis\", \"election_results.txt\")\n",
    "with open(output_file_path, 'w') as file:\n",
    "    file.write(\"Election Results\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n",
    "    for candidate, votes in candidates.items():\n",
    "        percentage = (votes / total_votes) * 100\n",
    "        file.write(f\"{candidate}: {percentage:.3f}% ({votes})\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n",
    "    file.write(f\"Total Votes: {total_votes}\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n",
    "    file.write(f\"Winner: {winner}\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71a2be32",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
