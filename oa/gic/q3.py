def budgetShopping(n, bundleQuantities, bundleCosts):
    m = len(bundleCosts)
    max_value = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for w in range(n + 1):
            if i == 0 or w == 0:
                max_value[i][w] = 0
            elif bundleCosts[i - 1] > w:
                max_value[i][w] = max_value[i - 1][w]
            else:
                max_value[i][w] = max(bundleQuantities[i - 1] + max_value[i][w - bundleCosts[i - 1]], max_value[i - 1][w])
    return max_value[m][n]

if __name__ == "__main__":
    n = 50
    bundleQuantities = [20, 19]
    bundleCosts = [24, 20]
    result = budgetShopping(n, bundleQuantities, bundleCosts)
    print(f"Test case 1 --- Expected : 40, Output : {result}")

     # Test case 2
    n = 10
    bundleQuantities = [1, 2, 3]
    bundleCosts = [2, 2, 2]
    result = budgetShopping(n, bundleQuantities, bundleCosts)
    print(f"Test case 2 --- Expected : 15, Output : {result}")
    
    # Test Case 3
    n = 100
    bundleQuantities = [10, 20, 30]
    bundleCosts = [5, 10, 15]
    result = budgetShopping(n, bundleQuantities, bundleCosts)
    print(f"Test case 3 --- Expected : 200, Output : {result}")
    
    