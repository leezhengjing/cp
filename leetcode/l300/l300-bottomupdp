def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def f(nums):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        maxLength = 0
        for i in range(1, n+ 1):
            ni = nums[i - 1]
            dp[i] = dp[0] + 1
            for j in range(1, i):
                nj = nums[j - 1]
                if nj < ni:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxLength = max(maxLength, dp[i])
        return maxLength
    return f(nums)