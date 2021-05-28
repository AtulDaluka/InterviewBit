class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        final_output_array = [1 for each in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if(nums[j]<nums[i]):
                    final_output_array[i] = max(1 + final_output_array[j],final_output_array[i])   
        print(final_output_array)
        return max(final_output_array)
