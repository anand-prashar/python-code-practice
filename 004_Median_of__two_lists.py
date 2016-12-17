'''
Created on Dec 7, 2016
# assume Both lists are sorted

@author: anand
'''
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    
    sumM = len(nums1)+len(nums2)
    mergeAIndex = sumM /2
    if sumM %2 ==0:
        evenMerge = True
    else:
        evenMerge = False
    
    i=0; n1Index = 0; n2Index = 0; m1 = None; m2 = None
    
    while i<= mergeAIndex:  
        if evenMerge:
            m1 = m2
            
        if n1Index< len(nums1) and n2Index< len(nums2):
            if ( nums1[n1Index] < nums2[n2Index]):
                m2 = nums1[n1Index]
                n1Index+=1
            else:
                m2 = nums2[n2Index]
                n2Index+=1
        elif n1Index< len(nums1):
            m2 = nums1[n1Index]
            n1Index+=1
        else:
            m2 = nums2[n2Index]      
            n2Index+=1      
        i+=1  
    
    if evenMerge: return float(m1+m2)/2
    else:         return float(m2)    
  
    
print findMedianSortedArrays([], [1,2])    
            