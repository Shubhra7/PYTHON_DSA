def getMaximumDistinctCount(a, b, k):
    # Step 1: Find the distinct elements in array 'a'
    distinct_in_a = set(a)
    swapable_place = len(a)-len(distinct_in_a)
    print(swapable_place)
    
    # Step 2: Find the elements in array 'b' that are not in 'a'
    distinct_in_b = set(b)
    
    # Step 3: Find potential new elements we can add to 'a' by swapping with 'b'
    new_elements = distinct_in_b - distinct_in_a
    print(new_elements)
    
    # Step 4: The number of swaps we can do is the minimum of k or the number of new elements
    max_new_distinct = min(len(new_elements), k,swapable_place)
    
    # Step 5: Return the number of distinct elements in 'a' after k swaps
    return len(distinct_in_a) + max_new_distinct

# Example Usage

a = [ 3, 3, 2,2]
b = [1,4,5]
k = 3
print(getMaximumDistinctCount(a, b, k))  # Output: 4