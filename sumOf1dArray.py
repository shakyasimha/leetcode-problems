### Add all elements of 1d array
import numpy as np 

def add1dArray(arr):
    """
        For example
        
        arr = [3,1,2,10,1]

        It 1:
            sum <- arr[1]+arr[0] = 1+3 = 4
            arr[1] <- 4
            arr = [3,4,2,10,1]
            
        It 2:
            sum <- arr[2]+arr[1] = 2+4 = 6
            arr[2] <- 6
            arr = [3,4,6,10,1]
            
        It 3:
            sum <- arr[3]+arr[2] = 10+6 = 16 
            arr[3] <- 16 
            arr = [3,4,6,16,1]
            
        It 4:
            sum <- arr[4]+arr[3] = 1+16 = 17
            arr[4] <- 17
            arr = [3,4,6,16,17]
    """
    
    total = 0 
    print(f"Array passed to the function: {arr}")
    
    ## Creates an updated array full of 0s but the same length and data type as the original array
    updated_arr = np.zeros(len(arr), dtype=arr.dtype)
    
    for i in range(0, len(arr)):
        ## First element will be the same for both arrays
        if i==0:
            updated_arr[i] = arr[i]
        else:
            total = arr[i]+arr[i-1]
            arr[i] = total
            print(f"Iteration {i}: {arr}")
            
    return arr 

if __name__ == "__main__":
    arr = np.random.randint(low=0, high=100, size=10)
    
    result = add1dArray(arr)
    print(f"Generated array: {arr}")
    print(f"Final array: {result}")