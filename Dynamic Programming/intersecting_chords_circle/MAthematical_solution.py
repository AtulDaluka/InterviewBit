import math

class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        x = math.factorial(2*A)
        y = math.factorial(A)
        z = math.factorial(A+1)
        result = ((x//(z*y)))%(pow(10,9) + 7)
        return result
    
    # def Factorial(self,m):
    #     dp = [0 for each in range(m+1)]
    #     dp[0]=dp[1] =1
    #     for x in range(2,m+1):
    #         dp[x] =x*dp[x-1]
    #     return(dp)

    # def chordCnt(self,n): # best O(n)
    #     dp = self.Factorial(2*n)
    #     return((dp[2*n]//(dp[n]*dp[n+1]))%((10**9)+7))
