def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def f(i, nums, memo):
        global lis
        if i == 0:
            return 0
        if memo[i] != 0:
            return memo[i]
        maxLength = f(0, nums, memo) + 1
        ni = nums[i - 1]
        for j in range(1, i):
            nj = nums[j - 1]
            f_of_j = f(j, nums, memo)
            if nj < ni:
                maxLength = max(maxLength, f_of_j + 1)
        lis = max(lis, maxLength)
        memo[i] = maxLength
        return maxLength
    global lis
    lis = 0
    n = len(nums)
    memo = [0] * (n + 1)
    f(n, nums, memo)
    return lis

if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lengthOfLIS(nums))
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(lengthOfLIS(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(lengthOfLIS(nums))
    
    