def printSubarr(lst,toggles=None,i=0):
    if toggles==None:
        toggles = [0]*len(lst)
    
    if i >= len(lst):
        subset = [str(lst[i]) for i in range(len(lst)) if toggles[i]==1]
        print("{"+", ".join(subset)+"}")
    else:
        toggles[i]=0
        printSubarr(lst,toggles,i+1)
        toggles[i]=1
        printSubarr(lst,toggles,i+1)

printSubarr([1,2,3])

#------------
#---------correct---------

def print_all_subarrays(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start, n):
            # Slicing to get the subarray
            subarray = arr[start:end+1]
            print(subarray)

# Example usage
array = [1, 2, 3]
print("All subarrays:")
print_all_subarrays(array)
