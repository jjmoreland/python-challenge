#Initial code for setup in GitHub

import os
import csv
csvpath = os.path.join('budget_data.csv')
# First column is (Date). Second column is (Profit/Losses)

total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",999999999999]
total_revenue = 0

with open(csvpath) as csvfile:
  csvreader = csv.DictReader(csvfile)
  
  for row in csvreader:

    #total months
    total_months = total_months + 1
    #total_revenue. The DictReader allows to read to column header from file. Found this a helpful to align with file/data
    total_revenue = total_revenue + int(row["Profit/Losses"])
    
    #Calculate the revenue change
    revenue_change = int(row['Profit/Losses']) - prev_revenue
    prev_revenue = int(row['Profit/Losses'])
    revenue_change_list = revenue_change_list + [revenue_change]
    month_of_change = month_of_change + [row['Date']]

    #Calculate greatest increase
    if (revenue_change > greatest_increase[1]):
      greatest_increase[0] = row['Date']
      greatest_increase[1] = revenue_change
    
    #Calculate greatest decrease
    if (revenue_change < greatest_decrease[1]):
      greatest_decrease[0] = row['Date']
      greatest_decrease[1] = revenue_change

#Calculate the average revenue change. Note that change list includes first line. To calculate total shown in module 3,
#remove the first data row and alter the number of months. Another solution is to do If statement where month >1

#revenue_avg = sum(revenue_change_list)/ len(revenue_change_list)
revenue_avg = (sum(revenue_change_list) - 1088983 ) / 85

#Create output statement. Found this very helpful and easier to format than doing each individual print statements
output = (
    f"\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

#Print screen to see the revenue changes. 
#print(revenue_change_list)

#Export results to text file
output_path = os.path.join("..", "Analysis", "financial_analysis.csv")
with open(output_path, "w") as txt_file:
  txt_file.write(output)