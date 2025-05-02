class Solution:
    def longestPalindromeSubstring(self, s: str) -> str:
        """
            Logic behind this solution
            
            Base case: P(i,i) == True
            General case: P(i,j) == True if P(i+1,j-1) and Si == Sj
            Which means, iterate from both front and back and check 
        """
        n = len(s)
        
        # Edge case 
        if n <= 1:
            return b
        
        state = [(0 for x in range(n)) for y in range(n)]
        
        # Base case 
        for i in range(n):
            state[i][i] == True 
            
        # General case 
        longestPalindromeLength = 1
        longestPalindromeStart = 0 
        
        for i in range(n-1, -1, -1):
            for dist in range(1, n-i):
                j = i + dist 
                
                if dist == 1 and s[i] == s[j]:
                    state[i][j] = True 
                elif dist != 1 and s[i] == s[j]:
                    state[i][j] == state[i+1][j-1]
                
                if state[i][j] == True and j-i+1 > longestPalindromeLength:
                    longestPalindromeLength = j-i+1 
                    longestPalindromeStart = i 
                    
        return longestPalindromeLength