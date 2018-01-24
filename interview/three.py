# Question 3

"""
    Which color is the median?
"""
from numpy import median

from data import dataset
from custom import sortMethod2, sortMethod, arranger


def main():
    pass
    theData = sortMethod2(sortMethod(dataset()))
    print theData

    sorted_list = arranger(theData.itervalues())
    print sorted_list

    def medianFinder(theList, theData):
        median_number = median(theList)
        median_colour = ""
        for colour in theData:
            if theData[colour] == median_number:
                median_colour = colour
                break
        return median_colour

    print medianFinder(sorted_list, theData)


if __name__ == "__main__":
    main()
