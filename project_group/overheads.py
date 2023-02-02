# imports csv and paths to work together with the csv files while managing file paths
# file path for 'overheads-day-90.csv' is stored in 'fp' variable
# whereas 'summary_report.txt' is stored in 'fp_report' variable

from pathlib import Path
import csv
fp = Path.cwd()/"C:\PFB\poppin_TC04_PFB\csv_reports\overheads-day-90.csv"
fp_report = Path.cwd()/"summary_report.txt"

'''
this function calculates the highest overhead category from the csv file 'overheads-day-90.csv'
it reads the data from the file and loops through each row to find the category with the highest overhead
value - the highest overhead category and its value are then stored in the variables 'highest_category' 
and 'highest-overhead' respectively
'''

def overhead_function(currency):

    # opens file located at path 'fp' in read mode and stores the file object in variable 'file'
    with fp.open(mode='r', encoding='UTF-8', newline='') as file:
        # creates a csv reader object from the file object
        reader = csv.reader(file)
        # skip header
        next(reader)

        # initialising the variables for 'highest_catgeory' and 'highest_overhead'
        highest_category = ''
        highest_overhead = 0.00

        # looping through each for in the file 
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

# Write the result string to the file located at path 'fp_report' in write mode then closing the file.
result = overhead_function(currency = 1)
with fp_report.open(mode='w', encoding='UTF-8', newline='') as filereport:
    filereport.write(result)
    filereport.close()
    
