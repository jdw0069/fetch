def totalAmountIsRound(totalPrice):
    cents = totalPrice.split(".")[1]
    if cents == "00":
        return 50
    return 0