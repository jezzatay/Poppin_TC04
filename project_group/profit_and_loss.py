#The program will compute the
#difference in the net profit column if net profit on
#the current day is lower than the previous day
from pathlib import Path
import csv
# csv file and its path
fp = Path.cwd()/"C:\PFB\project_group\csv_reports\profit-and-loss-usd.csv"
fp_report = Path.cwd()/"summary_report.txt"
'''
    This function reads in a CSV file containing data on net profit for each day. 
    The CSV file is located at "C:\PFB\project_group\csv_reports\profit-and-loss-usd.csv".
    The function checks if the net profit on each day is higher than that of the previous day.
    If the net profit on a day is lower, the day and the difference in net profit from the previous day are 
    recorded and stored in two separate lists.
    If there are no days with lower net profit, it will show that there is a net profit surplus, and that 
    the value is higher than the previous day.
    If there are days with lower net profit, the days and their respective differences are returned in a string
    that has been formatted.
    The returned result is then written to a file "summary_report.txt".
'''

# compute the difference in the net profit between two days in a given csv file 
# and return the result in the form of a string using the 'for-loop'
def profitloss_function(currency):
    # opening the profit and loss csv file
    with open(r"C:\PFB\project_group\csv_reports\profit-and-loss-usd.csv", "r") as file:
        reader = csv.reader(file)
        for item in reader:
            print (item)
            # assigning empty lists to store which day, its profits, the day deficit, and the profits deficit. 
            day = []
            profit = []
            day_deficit = []
            profits_deficit = []
            # to store the output message
            text_return = ''
        
        for count, row in enumerate(reader):
            day.append(row[0])
            profit.append(float(row[1]))

            if count > 0:
                if profit[count-1] > profit[count]:
                    day_deficit.append(row[0])
                    profits_deficit.append(profit[count-1] - int (row[4]))

    deficit_count = len(day_deficit)
    if deficit_count == 0:
        text_return = '[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n'
    else:
        a = 0
        while a < deficit_count:
           text_return = text_return + '[PROFIT DEFICIT] DAY {:.1f}, AMOUNT: USD{:.0f}\n'.format(int(day_deficit[1]),profits_deficit[a]*currency)
           
    return(text_return)
    print(text_return)    


result = profitloss_function(currency = 1)
with open(fp_report, 'a') as filereport:
    filereport.write(result)
    filereport.close()


