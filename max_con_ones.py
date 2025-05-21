class Solution:
    def longestOnes(self, nums: list[int], k: int) -> list:
        left = 0
        zero_count = 0
        max_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count = zero_count + 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count = zero_count - 1
                left= left + 1
                
            max_count = max(max_count, right-left+1)
        return max_count
    
obj = Solution()
print(obj.longestOnes(nums=[0,0,0,0,0,1], k=5))