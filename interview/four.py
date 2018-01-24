# Question 4

"""
   BONUS Get the variance of the colors
"""

from numpy import var

from data import dataset
from custom import sortMethod2, sortMethod, arranger


def main():
    pass
    theData = sortMethod2(sortMethod(dataset()))
    print theData

    sorted_list = arranger(theData.itervalues())
    print sorted_list

    def varianceCal(theList):
        var_val = var(theList)
        return int(var_val)

    print "The variance value: " + str(varianceCal(sorted_list))


if __name__ == "__main__":
    main()

