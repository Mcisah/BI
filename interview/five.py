# Question 5

"""
   BONUS if a colour is chosen at random, what is the probability that the color is red?
"""

from data import dataset
from custom import sortMethod2, sortMethod, arranger


def main():
    pass
    theData = sortMethod2(sortMethod(dataset()))
    print theData

    def probabilty(colour, theData):
        value = theData['RED']
        sorted_list = arranger(theData.itervalues())
        print sorted_list
        summation = sum(sorted_list)
        prob = float(value)/summation
        return "The probability of choosing " + colour + " at random is " + str(prob)

    print probabilty("RED", theData)


if __name__ == "__main__":
    main()
