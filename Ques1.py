#q1 for chaabi backend assigment This is selection sort which is implemented O(n^2) as we keep track of min element in each 
#iteration from i to N

def selectionSort(arr):
    
    for i in range(len(arr)):
        mi = i # min index defined as first index which will be updated further more
 
        for j in range(i+ 1, len(arr)):
            # the below if condition is to check whether the element is less or more than update or min indes
            if arr[j] < arr[mi]:
                mi = j
         # the minimum value's index which we get will be swapped with the ith position this will be repeated till the array is sorted
        (arr[i], arr[mi]) = (arr[mi], arr[i])
        
    
        
arr=list(map(int,input().strip().split()))
(selectionSort(arr))
print(arr)