### Add all elements of 1d array
import numpy as np 

def add1dArray(arr: np.ndarray):
    sum = 0 
    
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
    for i in range(1, len(arr)):
        sum = arr[i]+arr[i-1]
        arr[i] = sum 
        
    return arr 

if __name__ == "__main__":
    arr = np.random.randint(low=0, size=10)
    print(arr)
    
    sum = add1dArray(arr)
    print(sum)