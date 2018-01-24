def sortMethod(data):  # sorts the entries in the dataSet into one single list
    newDataSet = []
    for day in data:
        for colour in data[day]:
            newDataSet.append(colour)

    return newDataSet


def sortMethod2(data):
    newDataSet = {}
    for colour in data:
        newDataSet[colour] = 1
        for otherColour in data:
            if otherColour == colour:
                newDataSet[colour] += 1
            else:
                pass
        newDataSet[colour] -= 1
    return newDataSet


def arranger(data):
    return sorted(data)
