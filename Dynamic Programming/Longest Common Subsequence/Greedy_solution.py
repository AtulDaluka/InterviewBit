class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pile_top = [1000000 for each in range(len(nums))]
        pile_length = [0 for each in range(len(nums))]
        for i in reversed(range(len(nums))):
            for j in range(len(pile_top)):
                if(pile_top[j]>nums[i]):
                    pile_length[j] += 1
                    pile_top[j] = nums[i]
                    print(pile_top,pile_length)
                    break
        return max(pile_length)
