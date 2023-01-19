def isPurchaseDayOdd(purchaseDate):
    day = purchaseDate.split("-")
    if int(day[2]) %2 != 0:
        return 6
    return 0
