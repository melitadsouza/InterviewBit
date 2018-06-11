class Solution:

    # @param A : list of list of integers
    # @return the same list modified
    #solution 1
    def rotate(self, A):
        return zip(*A[::-1])
    
    #solution 2
    def rotate1(A):
    soln = [row[:] for row in A]
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = soln[len(A)-1-j][i]
    return A
