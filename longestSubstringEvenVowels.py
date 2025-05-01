# Problem defintion:
# Find the longest substring containing vowels in even counts.
# For example: "eleetminicoworoep", the output is 13

class Solution:
    def findLongestSubstring(self, s: str) -> int: 
        charSet = set()  # charSet = stores a substring with non-repeating characters
        n = len(s)       # length of the string
        l = 0            # index of left side of sliding window 
        max_length = 0   # maximum length of recurring substring

        """
            Logic behind this: 
            - r => rightmost index of the sliding window
            - if s[r] is in charSet, then the window is slided, removing the leftmost character and adding the rightmost character
            - the same process is repeated until the rightmost index reaches the end of the string
            - maximum length is calculated by comparing the current length of the substring and (r-l+1)
        """
        for r in range(n):  # r is the rightmost index of the sliding window 
            if s[r] in charSet: 
                charSet.remove(s[l])
                l += 1
                charSet.add(s[r])
            max_length = max(max_length, r - l + 1)
            
        return max_length 
    
if __name__ == "__main__":
    s = input("Enter any string: ")
    output = findLongestSubstring(s)
    print(output)