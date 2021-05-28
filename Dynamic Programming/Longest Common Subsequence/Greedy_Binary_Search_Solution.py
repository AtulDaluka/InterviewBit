class Solution:
    
    def upperbound(self, arr, num):
        left = 0
        right = len(arr)-1
        while(left<=right):
            mid = int((left+right)/2)
            if(arr[mid]<=num):
                left = mid+1
            else:
                right = mid
        return left
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        pile_top = [1000000 for each in range(len(nums))]
        pile_length = [0 for each in range(len(nums))]
        for i in (range(len(nums))):
            # for j in range(len(pile_top)):
            j = self.upperbound(pile_top,nums[i])
            # if(pile_top[j]>=nums[i]):
            print(j)
            pile_length[j] += 1
            pile_top[j] = nums[i]
                # print(pile_top,pile_length)
                # break
        count = 0
        for j in range(len(pile_length)):
            if(pile_length[j]!=0):
                count += 1
        return count
