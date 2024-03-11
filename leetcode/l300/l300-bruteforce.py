def generateSubsets(nums):
    n = len(nums)
    res = [[]]
    def dfs(start_index, path):
        if start_index == n:
            res.append(path)
            return
        dfs(start_index + 1, path + [nums[start_index]]) # include nums[start_index]
        dfs(start_index + 1, path) # do not include nums[start index]
    dfs(0, [])
    return res

def isIncreasing(arr):
    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:
            return False
    return True 

def longest_sub_len(nums):
    subsets = generateSubsets(nums)
    maxLength = 0
    for subset in subsets:
        if isIncreasing(subset):
            maxLength = max(maxLength, len(subset))
    return maxLength

if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(longest_sub_len(nums))
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(longest_sub_len(nums))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(longest_sub_len(nums))
    
    