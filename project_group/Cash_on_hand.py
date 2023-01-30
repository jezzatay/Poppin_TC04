#The program will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
from pathlib import Path
import csv
# csv file and its path
fp = Path.cwd()/"C:\PFB\project_group\csv_reports\cash-on-hand-usd.csv"
fp_report = Path.cwd()/"summary_report.txt"

'''
This function is to find out whether there was a cash surplus or deficit and calculates how much different
it is as compared the that of the previous day
'''
def coh_function(currency):
    # reading the csv file to include the profit and quantity
    with fp.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        for item in reader:
            print (item)

        # creating lists to store the days, cash, days deficit, cash defficit and count to the total record.
            day = []
            cash = []
            day_deficit = []
            cash_deficit = []
            count = 0
        # to return the outcome the string will give
            text_return = ''

        # adding the day and cash back to the empty list as a list.
        for row in reader:
            # this is for the day in column 0
            day.append(row[0])
            # row[1] is for cash in column 1
            cash.append(float[row[1]])

            for i in range(len(cash)-1, 0, -1):
                if cash[i-1] > cash[i]:
                    day_deficit.append(row[0])
                    cash_deficit.append(cash[i-1] - float(row[1]))

    # 
    deficit_count = len(day_deficit)
    if deficit_count == 0:
        text_return = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        
    else: 
        a = 0
        while a < deficit_count:
            text_return = text_return + '[CASH DEFICIT] DAY {:.1f}, AMOUNT: USD{:.0f}\n'.format(int(day_deficit))
    
    return text_return  
    print (text_return)
    file.close()

result = coh_function(currency = 1)
with open(fp_report, 'a') as filereport:
    filereport.write(result)
    filereport.close()

