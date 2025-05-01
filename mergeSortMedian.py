"""
    Problem definition:
    
    Given two lists of integers, find the median of the two sorted arrays.
    
    Example:
    
    - Input: nums1 = [1, 3], nums2 = [2]
    - Output: 2.00000
    - Explanation: merged array = [1, 2, 3] => median = 2.0
    - Input: nums1 = [1, 2], nums2 = [3, 4]
    - Output: 2.50000
    - Explanation: merged array = [1, 2, 3, 4] => median = (2 + 3) / 2 = 2.5
    
    
    Hint: 
    
    - For median, if the lenght of the array is even, the median is the average of the two middle elements.
    - If the length of the array is odd, the median is the middle element.
"""
from typing import List 

class Solution:
    def mergeAndFindMedian(self, A: List[int], B: List[int]) -> List[int]:
        """
            Now my strategy here:
            
            - First, merge sort two lists A and B;
            - After merge sorting the two lists, find median by comparing the final length of the resulting array
        """
        
        # Merge sort begins here
        m = len(A)
        n = len(B)
        C = []      # Resulting list 
        i = 0; j = 0
        
        while i < m and j < n:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < m:
            C.append(A[i])
            i += 1 
        while j < n:
            C.append(B[j])
            j += 1
            
        # After finishing merge sort, we find median
        k = len(C)
        median = 0 
        
        if k % 2 == 0: 
            median = (C[k // 2 - 1] + C[k // 2]) / 2
        else:
            median = C[k // 2]
            
        return median          
        