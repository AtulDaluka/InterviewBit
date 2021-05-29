class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        result_array = [0 for each in range(A)]
        for i in range(len(result_array)):
            if(i==0):
                result_array[i] = 1
            elif(i==1):
                result_array[i] = 2
            else:
                result_array[i] = result_array[i-1] + result_array[i-2] + A - 1
        return result_array[A-1]
