class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        if(A==1):
            return 1
        elif(A==2):
            return 2
        else:
            return self.chordCnt(A-1)+self.chordCnt(A-2)+A-1
