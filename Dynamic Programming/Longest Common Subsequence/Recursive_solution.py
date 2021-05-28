class Solution:
    
    def helperLengthOfLIS(self, nums, n):
        max_val = 1
        if(n==0):
            return max_val
        else:
            for j in range(n):
                if(nums[j]<nums[n]):
                    val = 1+self.helperLengthOfLIS(nums, j)
                    # print(nums[j],nums[n-1],j, val, max_val)
                    max_val = max(max_val, val)
            return max_val
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        final_val = 1
        for i in range(len(nums)):
            val = self.helperLengthOfLIS(nums, i)
            final_val = max(final_val, val)
        return final_val
