# Problem defintion:
# Find the longest substring containing vowels in even counts.
# For example: "eleetminicoworoep", the output is 13

def findLongestSubstring(s: str) -> int:
    
    # Vowel masking is done in a way: 
    # uoiea = 00000 (5-bit), if a vowel occurs once, then the value is set to 1
    # For example: if a appears 1 times, then the mask becomes 00001, if i appears 1 times, then 00100
    vowel_to_bit = {
        'a': 1,
        'e': 2,
        'i': 4,
        'o': 8,
        'u': 16
    }
    
    # Mask map to store the first occurence of each mask
    # Base case: 0 at index -1 
    # mask_map: {mask: idx}
    mask_map = {0: -1} 
    
    mask = 0 
    max_len = 0 
    
    for i, char in enumerate(s):
        if char in vowel_to_bit:
            mask ^= vowel_to_bit[char]
            
        if mask in mask_map: 
            max_len = max(max_len, i - mask_map[mask])
        else: 
            mask_map[mask] = i 
    
    return max_len 

if __name__ == "__main__":
    s = input("Enter any string: ")
    output = findLongestSubstring(s)
    print(output)