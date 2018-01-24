# Question 2

"""
    Which color is mostly worn throughout the week?
"""

from data import dataset
from custom import sortMethod, sortMethod2


def main():
    pass

    def modeFinder(theArray):
        colourCount = sortMethod2(theArray)
        print colourCount
        colourName = ""
        for colour in colourCount:
            colourGreater = False
            for otherColour in colourCount:
                if colour == otherColour:
                    pass
                else:
                    print "Comparing " + colour + " with " + otherColour
                    if colourCount[colour] > colourCount[otherColour]:
                        colourGreater = True
                        print colour, " is worn more often than ", otherColour
                    else:
                        colourGreater = False
                        print colour, " is worn less often than ", otherColour
            if colourGreater == True:
                colourName = colour
                break
        return "|\n|\n|\nThe " + colourName + " color is worn the most."
    print(sortMethod(dataset()))
    print modeFinder(sortMethod(dataset()))


if __name__ == "__main__":
    main()
