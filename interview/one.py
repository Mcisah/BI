# Question 1

"""
    Which color of shirt is the mean color?
"""
from numpy import mean

from data import dataset
from custom import sortMethod2, sortMethod, arranger


def main():
    pass
    theData = sortMethod2(sortMethod(dataset()))
    print theData

    meanData = arranger(theData.itervalues())
    print meanData

    def meanFinder(theList, theData):
        mean_number = round(mean(theList))
        mean_colour = []
        for colour in theData:
            if theData[colour] == mean_number:
                mean_colour.append(colour)
            else:
                pass

        return mean_colour

    print "The mean colour(s) are: "
    for colour in meanFinder(meanData, theData):
        print colour


if __name__ == "__main__":
    main()