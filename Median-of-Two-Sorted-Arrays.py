# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:19:27 2020

@author: -
"""

# 4. Median of Two Sorted Arrays

#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#You may assume nums1 and nums2 cannot be both empty.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        d = []
        d = nums1 + nums2
        d.sort()
        
        if len(d)%2 == 0:
            if len(d)/2 > round(len(d)/2):
                return ((d[round(len(d)/2)] + d[round(len(d)/2)+1])/2)
            else:
                return ((d[round(len(d)/2)] + d[round(len(d)/2)-1])/2)
        else:
            return d[int(len(d)/2)]
        
        
        
        
        
if __name__ == "__main__":
    

    
    nums1 = [1, 3]
    nums2 = [2, 4]
    
    a = Solution().findMedianSortedArrays(nums1, nums2)
    print(a)