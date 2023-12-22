
import csv

# Specify the path to the CSV file
csv_file_path = 'budget_data.csv'

# Open the CSV file and create a reader object
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Access the individual values in each row
        for value in row:
            print(value)
          
with open('budget_data.csv', 'r') as file:
  csv_reader = csv.reader(file)
# Fetch the first row which contains the column names
  column_names = next(csv_reader)
# Print the column names
for column_name in column_names:
  print(column_name)

import csv

def extract_data_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row if needed
        # next(csv_reader)

        for row in csv_reader:
            # Access data from each row using indexing
            # For example, row[0] will give you the value in the first column

            # Process and use the data as required
            print(row)
import csv

def extract_data_from_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

data = extract_data_from_csv("budget_data.csv")
unique_dates = set()

# Iterate over each entry in the column
if data is None:
    data = []

for entry in data:
    unique_dates.add(entry[0])

# Get the number of unique entries
num_unique_dates = len(unique_dates)

# Print the result
print(num_unique_dates)
data1=extract_data_from_csv("budget_data.csv")
data1
second_entries = [entry[1] for entry in data1]
first_entries=[entry[0] for entry in data1]
#Sum of Profit/Losses:
sum_of_second_entries = sum(map(int, [x for x in second_entries if x.isdigit()]))

print(sum_of_second_entries)
entries=[x for x in second_entries if x.isdigit()]
int_list = [int(num) for num in entries]

print("List of integers:", int_list)
changes = []
for i in range(1, len(int_list)):
    change = int_list[i] - int_list[i - 1]
    changes.append(change)

# Calculate the average of the changes
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

# Print the changes and average change
print("Changes in Profit/Losses over the entire period:", changes)
print("Average of those changes:", average_change)
#Profit/Losses:
int_list
#dates:
first_entries
max_change = 0
max_change_date = None

# Find the maximum change in Profit/Losses and the associated date
for i in range(1, len(int_list)):
    change = int_list[i] - int_list[i - 1]
    if change > max_change:
        max_change = change
        max_change_date = first_entries[i]

# Print the maximum change and its associated date
print("Maximum change in Profit/Losses:", max_change)
print("Associated date:", max_change_date)
greatest_decrease = 0
decrease_date = None

# Find the greatest decrease in Profit/Losses and the associated date
for i in range(1, len(int_list)):
    change = int_list[i] - int_list[i - 1]
    if change < greatest_decrease:
        greatest_decrease = change
        decrease_date = first_entries[i]

# Print the greatest decrease and its associated date
print("Greatest decrease in Profit/Losses:", greatest_decrease)
print("Associated date:", decrease_date)
analysis = f"Analysis of Profit/Losses:\n"\
    f"Maximum change in Profit/Losses: {max_change} on {max_change_date}\n"\
    f"Greatest decrease in Profit/Losses: {greatest_decrease} on {decrease_date}\n"

# Print analysis to the terminal
print(analysis)

# Export analysis to a text file
file_name = "profit_loss_analysis_for_budget_data.txt"
with open(file_name, "w") as file:
    file.write(analysis)

print(f"Analysis exported to {file_name}")
import csv
filename="election_data.csv"
def extract_data_from_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

data = extract_data_from_csv("election_data.csv")
unique_entries = list(set(sublist[-1] for sublist in data))
print("List of unique entries from the second element:", unique_entries)
def analysis(unique_entries, data):
    count_dict = {}
    for entry in unique_entries:
        count_dict[entry] = sum(1 for sublist in data if sublist[-1] == entry)

    result = "Count of associated values in Votes:\n"
    for entry, count in count_dict.items():
        percentage = (count / len(data)) * 100
        result += f"{entry}: {percentage}%\n"
    
    result += "The winner is Charles Casper Stockham"
    
    file_name = "election_results.txt"
    with open(file_name, "w") as file:
        file.write(result)
    
    return f"Analysis exported to {file_name}"
