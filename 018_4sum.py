'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
import itertools
### GIVEN SOLN:
#===============================================================================
# class Solution(object):
#     def fourSum(self, nums, target):
#         nums.sort()
#         results = []
#         self.findNsum(nums, target, 4, [], results)
#         return results
#     
#     def findNsum(self, nums, target, N, result, results):
#         if len(nums) < N or N < 2: return
#     
#         # solve 2-sum
#         if N == 2:
#             l,r = 0,len(nums)-1
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                     while r > l and nums[r] == nums[r + 1]:
#                         r -= 1
#                 elif nums[l] + nums[r] < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else:
#             for i in range(0, len(nums)-N+1):   # careful about range
#                 if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
#                     break
#                 if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
#                     self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
#         return  
#===============================================================================
     
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums = sorted(nums)
        if len(nums)<1 or nums[0]*4>target or nums[-1]*4< target:
            return []
        
        nc4 = itertools.combinations(nums,4)
        mapList = []
        for candidateList in nc4:
            if sum(candidateList) == target:
                mapList.append(tuple(sorted(candidateList)))
                 
        mapList = list(set(mapList))
        for i in range(len(mapList)):   
            mapList[i] = list(mapList[i])
         
        return sorted(mapList)    

obj = Solution()
l = [-490,-481,-471,-467,-453,-450,-446,-440,-437,-424,-423,-391,-384,-373,-358,-332,-318,-314,-311,-309,-299,-279,-270,-257,-243,-208,-205,-171,-153,-147,-142,-138,-129,-99,-20,-19,17,30,44,82,86,93,122,125,138,139,158,169,175,181,199,200,203,203,205,225,248,272,277,306,334,335,337,338,342,344,359,396,403,405,412,434,437,439,440,441,443,446,446,457,465,468,473,496]

print obj.fourSum(l , 1896)
    