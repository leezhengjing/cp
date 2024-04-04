import sys
def count_ways(sum, m, t, dp):
    # sum = current sum of time
    # m = target number of minutes
    # t = array of courses time
    # dp = memo array
    if sum == m:
        return 1
    
    if sum > m:
        return 0
    
    if dp[sum] != -1:
        return dp[sum]
    
    res = 0
    for i in range(len(t)):
        res += count_ways(sum + t[i], m, t, dp)
    
    dp[sum] = res
    return res
    

def main():
    M = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    T = [int(sys.stdin.readline().strip()) for _ in range(N)]
    dp = [-1 for _ in range(M + 1)]
    print(count_ways(0, M, T, dp))
    
if __name__ == "__main__":
    main()