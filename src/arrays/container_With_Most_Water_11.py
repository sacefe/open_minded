'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
'''

from typing import List
# import matplotlib.pyplot as plt
# import cv2
# im= cv2.imread("/home/demo/sacode/practices/open_minded/arrays/pictures/question_11.jpg")  
# im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)
# plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2BGRA))

class Water_Containers():
# class Water_Containers():
    def maxArea(self, height: List[int]) -> int:
        n =len(height) - 1
        p1, p2 = 0, n
        maxContainer= float("-inf")
        while p1 < p2:
            area= (p2-p1) * min(height[p2], height[p1])
            maxContainer= max(maxContainer, area)
            if p2 > p1:
                p1 +=1
            else:
                p2 -=1
        return maxContainer      

if __name__ == "__main__":
    container= [1,8,6,2,5,4,8,3,7]
    objSol= Water_Containers()
    print( objSol.maxArea(	container ) )

