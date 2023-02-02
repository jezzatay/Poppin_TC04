# importng the csv and paths to work with the csv files and to manage file paths
# the file path for 'profit-and-loss-usd.csv' is stored in the 'fp' variable and 
# 'summary_report.txt' is stored in the fp_report' variable
from pathlib import Path
import csv
# csv file and its path
fp = Path.cwd()/"C:\PFB\poppin_TC04_PFB\csv_reports\profit-and-loss-usd.csv"
fp_report = Path.cwd()/"summary_report.txt"

'''
    This function reads in a CSV file containing data on net profit for each day. 
    The CSV file is located at "C:\PFB\poppin_TC04_PFB\csv_reports\profit-and-loss-usd.csv".
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
    with open(r"C:\PFB\poppin_TC04_PFB\csv_reports\profit-and-loss-usd.csv", "r") as file:
        reader = csv.reader(file)
        for item in reader:
            next(reader)
            print (item)

            # assign empty lists to store which day, its profits, the day deficit,
            # and the profits deficit. 
            day = []
            profit = []
            day_deficit = []
            profits_deficit = []
            # to store the output message
            text_return = ''

        # this calculates the profits, 'day' is being append to 'row[0]' 
        # and the profit is being converted to a float and appended to 'row[1]'
        for count, row in enumerate(reader):
            day.append(row[0])
            profit.append(float(row[1]))

            # checking if the current days profit is lower than the previous day's. If the value of the current day
            # is lower than the previous day's, it is then added to the list of days which has deficits and also
            # indicated the differences between the days
            if count > 0:
                if profit[count-1] > profit[count]:
                    day_deficit.append(row[0])
                    profits_deficit.append(profit[count-1] - int (row[4]))

# check if there is a deficit by counting the number of days with a deficit, being the list 'deficit_count'
# len(day_deficit). if 'deficit_count' equals to 0, it would mean that there is a net profit surplus for
# all of the days and returns 'text_return' with a message that says: 
#"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY".
# however if there is a deficit, the loop is being initiated to iterate all the deficit days and returns
#'text_return' with a message '[PROFIT DEFICIT] DAY: <day>, AMOUNT: <amount>' in the format:
#'(int(day_deficit[1]),profits_deficit[a]*currency)'
    deficit_count = len(day_deficit)
    if deficit_count == 0:
        text_return = '[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n'
    else:
        a = 0
        while a < deficit_count:
           text_return = text_return + '[PROFIT DEFICIT] DAY: {:.1f}, AMOUNT: USD{:.0f}\n'.format(int(day_deficit[1]),profits_deficit[a]*currency)

# returning text_return
    return text_return

# calling the function 'profitloss_function' with the variable 'currency' set to 1. It stores the
# returned value in the variable 'result'
# it then opens the file in append mode and writes the value of 'result' to it then finally closing the file.
result = profitloss_function(currency = 1)
with open(fp_report, 'a') as filereport:
    filereport.write(result)
    filereport.close()
    
    
    


