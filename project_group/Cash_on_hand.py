# importng the csv and paths to work with the csv files and to manage file paths
# the file path for 'cash-on-hand-usd.csv' is stored in the 'fp' variable and 
# 'summary_report.txt' is stored in the fp_report' variable
from pathlib import Path
import csv
fp = Path.cwd()/"C:\PFB\poppin_TC04_PFB\csv_reports\cash-on-hand-usd.csv"
fp_report = Path.cwd()/"summary_report.txt"

'''
This functions reads the CSV file, 'cash-on-hand.csv' and performs an analysis on the data to determine
whethere there is a cash surplus deficit on each day. The data in the CSV file contains the day and
cash balance for each day. This function calculates whether the cash balance on each day is greater
than the previous day. If the value is higher, the result is a cash surplus and if it is lower, the
result is a cash deficit. Each result will return a message,
'[CASH SURPLUS]  CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY' 
and '[CASH DEFICIT] DAY <day>, AMOUNT: USD<amount>' in the format (int(day_deficit)), respectively. 
'''
def coh_function(currency):

    # opening the CSV file to read
    with fp.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        for item in reader:
            # skip the header
            next(reader)

        # creating lists to store the days, cash, days deficit, cash defficit and count to the total record.
            day = []
            cash = []
            day_deficit = []
            cash_deficit = []
            count = 0

        # to return the outcome the string will give
            text_return = ''

        # Looping through the rows in the reader and appending the days and cash to its respective lists
        for row in reader:
            day.append(row[0])
            cash.append(float[row[1]])

            # Looping through the cash list in revers to check if the cash for each day is greater
            # than the previous day
            for i in range(len(cash)-1, 0, -1):
                if cash[i-1] > cash[i]:
                    day_deficit.append(row[0])
                    cash_deficit.append(cash[i-1] - float(row[1]))

    # To derive the number of deficit 
    deficit_count = len(day_deficit)

    # if the deficit count equals to 0, the text_return will be
    # '[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'
    if deficit_count == 0:
        text_return = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
    
    # If there is a deficit, it will loop through each deficit day and will append the results to the
    # 'text_return' string
    else: 
        a = 0
        while a in range(deficit_count):
            text_return = text_return + '[CASH DEFICIT] DAY {:.1f}, AMOUNT: USD{:.0f}\n'.format(int(day_deficit))
    
    # returning and printing 'text_return' and closing the file
    return text_return  
    print (text_return)
    file.close()


# 
result = coh_function(currency = 1)

# Opening the report file for appending and writing the result to the file, then finally closing the file.
with open(fp_report, 'a') as filereport:
    filereport.write(result)
    filereport.close()
