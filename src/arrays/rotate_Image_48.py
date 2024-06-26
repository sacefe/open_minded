'''
48. Rotate Image
Medium

17457

803

Add to List

Share
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
Accepted
1,761,383
Submissions

SOLUTION
Matrix       Matrix =   Matrix         Matrix
ORIGIA? ==>  ROTATE =  TRANSPONE then  REVERSE 
'''

from typing import List

class Rotate:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows= len(matrix)
        cols= len(matrix[0])
        #Transpone Matrix
        for i in range(rows):
            for j in range(i+1, cols, 1):
                matrix[i][j], matrix [j][i] = matrix [j][i], matrix[i][j]

        #reverse matrix
        for i in range (rows):
            for j in range (cols//2):
                temp = matrix[i][j]
                matrix[i][j] =  matrix [i][cols-1-j]
                matrix[i][cols-1-j] =temp



if __name__ == "__main__":
    ob = Rotate()
    matrix = [[1,2,3],[4,5,6],[7,8,9]] 
    print(matrix)
    ob.rotate(matrix)
    print(matrix)