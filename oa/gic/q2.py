def maxDifference(px):
    maxDiff = -1
    lowest = px[0]
    for price in px:
        if price < lowest:
            lowest = price
        maxDiff = max(price - lowest, maxDiff)
    if maxDiff == 0:
        maxDiff = -1
    return maxDiff