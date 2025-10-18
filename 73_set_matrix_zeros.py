# https://leetcode.com/problems/set-matrix-zeroes

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        numCol = len(matrix[0])
        zeroinFirstCol = False
        for i, row in enumerate(matrix):
            if matrix[i][0] == 0:
                zeroinFirstCol = True
            for j, column in enumerate(row):
                if matrix[i][j] == 0 and j != 0: 
                    #if j is zero, we gonna make the first element to become 0  
                    # and thus when we loop to make zeros later it turn the first 
                    # row to zero and make the whole row become zero
                    matrix[i][0] , matrix[0][j] = 0, 0

        for row in range(len(matrix) - 1, -1, -1): #backward to avoid overwriting the first row too early
            for col in range(numCol - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if zeroinFirstCol:
                matrix[row][0] = 0

        
