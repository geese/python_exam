#!/usr/bin/env python3
"""
Reads in a series of values input by the user.
Computes an alternating sum of all values entered. 
For example, if your programs reads
input:
    1 4 9 16 9 7 4 9 11
    then, it computes 1 - 4 + 9 - 16 + 9 -7 +4 -9 + 11 = -2
"""
import sys

def calc_alt_sum(values):
    """
    Calculates alternating sum of values in a list
    args:
        values:  a list of numbers
    returns:
        the sum (subtracts numbers in odd positions, adds numbers in even positions)
    """
    sum = values[0]  # set sum equal to first value
    for i in range(0, len(values)):
        if i + 1 != len(values):   # make sure index doesn't go out of range
            if i % 2 == 0:  # current index is even
                sum -= values[i+1]
            else:           # current index is odd
                sum += values[i+1]
    return sum



# Main function
def main():
    """
    Prompts the user to enter values one at a time,
    blank input to quit.
    Prints the alternating sum.
    """
    values = []
    value = 1

    while (value): #false if empty string
        print("Enter value (blank line to quit): ")
        value = input()
        if (value):
            values.append(int(value))

    #print(values)
    print("The alternating sum is {:.1f}".format(calc_alt_sum(values)))
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)









