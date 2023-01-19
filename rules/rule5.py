import math

def itemDescriptionIsMultipleOf3(items):
    pointTotal = 0
    
    for currentItem in items:
        strippedString = len(currentItem["shortDescription"].strip())
        if strippedString % 3 == 0:
            points = float(currentItem["price"]) * 0.2
            pointTotal += math.ceil(points)
    return pointTotal

