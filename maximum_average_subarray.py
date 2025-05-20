from numpy import mean
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        pos = 0
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(k, len(nums)):
            cur_sum = (cur_sum + nums[i] - nums[i-k])
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum/k
    
obj = Solution()
print(obj.findMaxAverage(nums=[1,12,-5,-6,50,3], k=4))