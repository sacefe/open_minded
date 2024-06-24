'''
3 sun
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.    
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
from typing import List

class Sum3():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        numsS= [x for x in nums]
        numsS.sort()
        triList= []

        def sumTri(i:int):
            seen = set()
            j = i + 1 
            while j < len(numsS):
                complement = -(numsS[i] + numsS[j])
                if complement in seen:
                    triList.append([numsS[i], numsS[j], complement])
                    while j+1 < len(numsS) and  numsS[j] == numsS[j+1]:
                        j +=1
                seen.add(numsS[j])
                j += 1


        for i in range(n):
            if nums[i] > 0:
                break
            if (i == 0 or nums[i] != nums[i-1]):
                sumTri(i)

        return triList

if __name__ == "__main__":
    obj = Sum3()
    nums = [-1,0,1,2,-1,-4]
    print(obj.threeSum(nums))  