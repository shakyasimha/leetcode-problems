# Given an integer x, return true if x is a  palindrome, and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

def isPalindrome(x: int) -> bool:
        digit_list = []
        temp = x
        palindrome_num = 0 
        
        ## For appending each digit of the number in the list
        while(temp > 0):
            digit_list.append(temp % 10)
            temp = temp // 10 
            print(f"digit: {digit_list}")
            print(f"temp: {temp}")
            
        exp_val = len(digit_list)
        
        for i in digit_list[::-1]:
            palindrome_num += (10**(exp_val-1))*i 
            exp_val -= 1 
        
        return x == palindrome_num
    
if __name__ == "__main__":
    num = int(input("Enter any number to check for palindrome: "))
    output = isPalindrome(num)
    print(output)
        