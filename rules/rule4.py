def everyTwoItems(itemsList):
    total = 0
    points = 0
    for i in itemsList:
        total += 1
        if total % 2 == 0:
            points += 5
    return points

    
    
