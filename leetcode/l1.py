def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashTable = {}
    for i, x in enumerate(nums):
        diff = target - x
        if diff in hashTable:
            return [hashTable[diff], i]
        hashTable[x] = i
    return

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(None, nums, target))