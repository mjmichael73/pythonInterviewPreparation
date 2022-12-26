def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
    return []


nums = [10, 14, 16, 17]
target = 26
print(twoSum(nums, target))