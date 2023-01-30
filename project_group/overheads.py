#The program will find the highest overhead category.
from pathlib import Path
import csv
fp = Path.cwd()/"C:\PFB\project_group\csv_reports\overheads-day-90.csv"
fp_report = Path.cwd()/"summary_report.txt"

def overhead_function(currency):
    with fp.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader) #skip header

        highest_category = ''
        highest_overhead = 0.00

        for row in reader:
            if float(row[1]) > highest_overhead:
                highest_category = row[0]
                highest_overhead = float(row[1])
        file.close()

# def format_result(highest_category, highest_overhead):
    text_return = '[HIGHEST OVERHEAD] {}: {:.2f}%\n'.format(highest_category.upper(), highest_overhead)
    

    return text_return
    print(text_return)
    file.close()

result = overhead_function(currency = 1)
with fp_report.open(mode='w', encoding='UTF-8', newline='') as filereport:
# with open(fp_report, 'w') as filereport:
    filereport.write(result)
    filereport.close()

