# 2670. Find the Distinct Difference Array

def distinctDifferenceArray(nums):

    prefixSet = set({})
    prefix = []
    for i in range(0, len(nums)):
        prefixSet.add(nums[i])
        prefix.append(len(prefixSet))


    suffixSet = set({})
    suffix = [0]*len(nums)
    for i in range(len(nums)-1, -1,-1):
        suffix[i] = len(suffixSet)
        suffixSet.add(nums[i])
    distinct = [0]*len(nums)
    for i in range(0, len(nums)):
        distinct[i] = prefix[i] - suffix[i]
    return distinct

print(distinctDifferenceArray([1,2,3,4,5]))
print(distinctDifferenceArray([3,2,3,4,2]))