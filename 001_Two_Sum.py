'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
You may assume that each input would have exactly one solution.
'''

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        useDictionary = {}
        pos = 0
        for element in nums:
            useDictionary.setdefault(element, [])
            useDictionary[element].append(pos)
            
            pos += 1
        
        pos = 0    
        for element in nums:
            if (target - element) in useDictionary:
                
                if (element == (target - element)):
                    if (len(useDictionary[element]) != 1):
                        return [ useDictionary[element][0], useDictionary[element][1] ]
                    else: 
                        pos += 1 
                        continue  
                return [pos, useDictionary[target - element][0] ]   
            pos += 1 
        return    


print twoSum([3, 2, 4, 3], 6)    
