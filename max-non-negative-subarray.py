class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        self.A = []
        
        
        maxSum = 0
        max_arr = []
        new_arr = []
        newSum = 0
        
        
        if A == []:
            return 0
        
        if max(A) < 0:
            return max_arr
        
        for i in range(len(A)):
            if A[i] >= 0:
                newSum += A[i]
                new_arr.append(A[i])
            else:
                newSum = 0
                new_arr = []
                
            if maxSum < newSum or maxSum == newSum and len(new_arr) > len(max_arr):
                maxSum = newSum
                max_arr = new_arr
                
        return max_arr
