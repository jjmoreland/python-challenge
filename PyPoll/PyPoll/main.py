import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# First column is the ballet ID. Second column is the county. Third column is the candidate's name

# We want to count how many candidates are in the election and their vote totals.

# Create an empty dictionary to hold the candidates and their counts
candidates = {}

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    total_candidates = 0
    for row in csvreader:
        
        total_candidates += 1
        # If candidate is already in the dictionary, increment the count else 
        # add the candidate to the dictionary
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

print('\n')
print('Election Results')
print('-----------------------------------------')
print('Total Votes:', total_candidates)
print('-----------------------------------------')
# Print the contents of the dictionary, the keys are the candidates and the values are the counts
# Here's an example of how to loop through a dictionary and print out the contents   
for key, value in candidates.items():
    print(f'{key} received {value} votes.')   
    
print('\n')
    
# Print out with percentages of the total
print('Candidate Percentages')
print('-----------------------------------------')
most_candidate = 0
most_candidate_type = ''
for key, value in candidates.items():
    print(f'{key}: {round(value/total_candidates*100,2)}% ({value})')   
    if value > most_candidate:
        most_candidate = value
        most_candidate_type = key
print('\n')
print('-----------------------------------------------------')        
print(f'The winner of the election is: {most_candidate_type} with {most_candidate}.')
print('-----------------------------------------------------')
print('\n')

# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("..", "Output", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    # Write the second row
    csvwriter.writerow(['Total Votes:', total_candidates])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow(['Total vote count per candidate: '])
    for key, value in candidates.items():
        csvwriter.writerow([f'{key} received {value} votes.'])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow(['Total percentage per candidate: '])
    for key, value in candidates.items():
        csvwriter.writerow([f'{key}: {round(value/total_candidates*100,2)}% ({value})'])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow([f'The winner of the election is: {most_candidate_type} with {most_candidate}.'])
    

