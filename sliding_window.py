# given a positive integer array nums and an integer k. We need to find the length of the longest subarray 
# that has a sum less than or equal to k. For this example, let nums = [3, 2, 1, 3, 1, 1] and k = 5.

class longestSubArray:
    def findSubArray(self, numsarray: list, arraySum: int):
        maxSubArrayLen = 0
        bestSubArray = []
        left = 0
        right = 0

        while right < len(numsarray):
            subArray = numsarray[left:right + 1]

            if sum(subArray) <= arraySum:
                if len(subArray) > maxSubArrayLen:
                    maxSubArrayLen = len(subArray)
                    bestSubArray = subArray
                right += 1
            else:
                left += 1
                if left > right:
                    right = left  # avoid invalid slice where left > right

        return maxSubArrayLen


# Test
nums = [3, 1, 1, 1, 1, 5]
obj = longestSubArray()
print(obj.findSubArray(numsarray=nums, arraySum=5))

    