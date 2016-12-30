'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dictionary = {}
        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            if temp not in dictionary:
                dictionary.setdefault(temp,[ strs[i] ])
            else:
                dictionary[temp ].append(strs[i])
        
        solution = []
        for values in dictionary.itervalues():
            solution.append(values)
        return solution

obj = Solution()
print obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 