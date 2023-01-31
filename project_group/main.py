# Importing the required files into the main file.
import Cash_on_hand, overheads, profit_and_loss
'''
This function runs three functions in a sequence to provide a complete report for Cash on Hand, Overheads
and Profit and Loss.
It imports three modules, 'Cash_on_hand', 'overheads', and 'profit_and_loss' to run their respective
functions
'''
def main():

    # setting currency = 1 USD
    currency = 1

    # Call to run three functions in a sequence
    Cash_on_hand.coh_function(currency)
    overheads.overhead_function(currency)
    profit_and_loss.profitloss_function(currency)

# executing the main function
main()
