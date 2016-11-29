#!/usr/bin/env python
"""

"""
import sys



def calc_assistance(income, kids):
    """
    Calculates amount of financial assistance based
    on annual household income and number of children.

    args:
        income: annual household income
        kids:   number of children
    returns:
        assistance amount
    """
    if income < 20000:
        return float(2000 * kids)
    if (income >= 20000 and income < 30000) and kids >= 2:
        return 1500 * kids
    if (income >= 30000 and income < 40000) and kids >= 3:
        return float(1000 * kids)




# Main function
def main():
    """
    Prompts the user to enter annual household income and number of children.
    Quits if user enters -1
    """
    
    income = ""
    while income != -1:
        print("What is the annual household income? (-1 to quit)")
        income = input()    #read keyboard input
        if income != -1:
            print("How many children?")
            kids = input()
            amount = calc_assistance(income, kids)
            print ("The assistance amount is ${:.2f}".format(0 if amount is None else amount))
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)







#http://www.noah.org/wiki/Python_starter_script


