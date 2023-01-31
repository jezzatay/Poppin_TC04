# importng the csv and paths to work with the csv files and to manage file paths
# the file path for 'overheads-day-90.csv' is stored in the 'fp' variable and 
# 'summary_report.txt' is stored in the fp_report' variable
from pathlib import Path
import csv
fp = Path.cwd()/"C:\PFB\project_group\csv_reports\overheads-day-90.csv"
fp_report = Path.cwd()/"summary_report.txt"

'''
This funcitons calculates the highest overhead category from the csv file 'overheads-day-90.csv'
it reads the data from the file and loops through each row to find the category with the highest overhead
value. The highest overhead category and its value are then stored in the variables 'highest_category' 
and 'highest-overhead' respectively. 
'''

def overhead_function(currency):

    # Opening the file located at path 'fp' in read mode, and storing the file object in variable 'file'
    with fp.open(mode='r', encoding='UTF-8', newline='') as file:
        # Create a csv reader object from the file object
        reader = csv.reader(file)
        # Skip header
        next(reader) 

        # Initialising the variables for 'highest_category' and 'highest_overhead'
        highest_category = ''
        highest_overhead = 0.00

        # Looping through each for in the file
        for row in reader:

            # If the overhead value in the current row is greater than the current highest overhead, it will
            # update highest category and highest overhead with the values in the current row. 
            if float(row[1]) > highest_overhead:
                highest_category = row[0]
                highest_overhead = float(row[1])
        # Closing the file
        file.close()
    # assigning a message to 'text_return'. The message being
    # '[HIGHEST OVERHEAD] <highest_category>: <highest_overhead>%' in the format:
    # (highest_category.upper(), highest_overhead)
    text_return = '[HIGHEST OVERHEAD] {}: {:.2f}%\n'.format(highest_category.upper(), highest_overhead)
    
    # returning and printing 'text_return'then closing the file
    return text_return
    print(text_return)
    file.close()

# Write the result string to the file located at path 'fp_report' in write mode then closing the file
result = overhead_function(currency = 1)
with fp_report.open(mode='w', encoding='UTF-8', newline='') as filereport:
    filereport.write(result)
    filereport.close()
