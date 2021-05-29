class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        
        n = len(A)
        dp_in = [1 for each in range(len(A))]
        dp_de = [1 for each in range(len(A))]
        
        for i in range(len(A)):
            for j in range(i):
                if(A[i]>A[j]):
                    dp_in[i] = max(1 + dp_in[j],dp_in[i])
                    
        for i in reversed(range(len(A))):
            for j in range(i+1,n-1):
                if(A[i]>A[j]):
                    dp_de[i] = max(1 + dp_de[j],dp_de[i])
        
        # print(dp_in,dp_de)
        result = 0
        for i in range(len(A)):
            result = max(result, dp_de[i]+dp_in[i]-1)
        
        return result
