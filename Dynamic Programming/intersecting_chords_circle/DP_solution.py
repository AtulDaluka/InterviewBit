class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        result_array = [0 for each in range(A+1)]
        result_array[0] = 1
        result_array[1] = 1
        # i = 0, length = 1, 1 pair, output 1
        # i = 1, j = 0, A = 2, result_array[0]*result_array[0]
        # i = 2, j = 0, A = 3, result_array[0]*result_array[1]
        # i = 2, j = 1, A = 3, result_array[1]*result_array[0]
        # i = 3, j = 0, A = 4, result_array[0]*result_array[2]
        # i = 3, j = 1, A = 4, result_array[1]*result_array[1]
        # i = 3, j = 2, A = 4, result_array[2]*result_array[0]
        for i in range(2,len(result_array)):
            for j in range((i)):
                result_array[i] = result_array[i] + result_array[j]*result_array[i-j-1]
        return (result_array[A]) % (10**9+7)
