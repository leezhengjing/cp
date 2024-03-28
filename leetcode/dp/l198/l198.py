class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [0, nums[0]]
        print(dp)
        # Let dp[i] state be the maximum amt of money that can be robbed including and up to the i-th house in nums. 
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i-1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[n-1][0], dp[n-1][1])
        
        # no_rob = 0
        # rob = 0
        # for num in nums:
        #     temp = max(no_rob, rob)
        #     rob = no_rob + num
        #     no_rob = temp
        # return max(no_rob, rob)
        # [[0, 1], [0, 0], [0, 0], [0, 0]]
        # [[0, 1], [0, 0], [0, 0], [0, 0]]

