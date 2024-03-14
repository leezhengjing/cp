# Bottom Up DP
def knapsack_weights_only_bottomup(weights):
    n = len(weights)
    total_sum = sum(weights)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for w in range(0, total_sum + 1):
            dp[i][w] = dp[i][w] or dp[i -1][w]
            if w >= weights[i - 1]:
                dp[i][w] = dp[i][w] or dp[i-1][w - weights[i-1]]
    ans = []
    for w in range(0, total_sum + 1):
        if dp[n][w]:
            ans.append(w)
    return ans

# Optimised Bottom Up DP
def knapsack_weights_only_bottomup_optimised(weights):
    n = len(weights)
    total_sum = sum(weights)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(2)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for w in range(0, total_sum + 1):
            dp[1][w] = dp[1][w] or dp[0][w]
            if w >= weights[i - 1]:
                dp[1][w] = dp[1][w] or dp[0][w - weights[i-1]]
        for w in range(0, total_sum + 1):
            dp[0][w] = dp[1][w]
    
    ans = []
    for w in range(0, total_sum + 1):
        if dp[0][w]:
            ans.append(w)
    return ans

if __name__ == "__main__":
    weights = [1, 3, 3, 5]
    expected = [0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12]
    # output = knapsack_weights_only_bottomup(weights)
    output = knapsack_weights_only_bottomup_optimised(weights)
    print("Expected: " + str(expected))
    print("Output:   " + str(output))
    if expected == output:
        print("PASS")