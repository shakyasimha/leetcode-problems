"""
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
    
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
"""

def addTwoNumbers(l1, l2):
    # What is happening here
    # l1 is being reversed, converted to string and then converted to integer
    # l2 is being reversed, converted to string and then converted to integer
    # l1 and l2 are added
    # the result is converted to string
    # the result is reversed
    # now the reversed string will be converted to a list of integers
    res = str(
        int("".join(
            map(str, l1[::-1])
        ))
        +int("".join(
            map(str, l2[::-1])
        ))
    )[::-1]
    
    result_list = [int(char) for char in res]
    
    print(result_list)
    

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
addTwoNumbers(l1, l2)
            
        
        
        
        
