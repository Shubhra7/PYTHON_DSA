# https://www.naukri.com/code360/problems/allocate-books_1090540
# https://www.youtube.com/watch?v=Z0hwjftStI4

"""
You are given an array arr[] of integers, where each element arr[i] 
represents the number of pages in the ith book. You also have an integer 
k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any 
student. In other words, out of all possible allocations, find the arrangement 
where the student who receives the most pages still has the smallest possible maximum.

Note: Return -1 if a valid assignment is not possible, and allotment should be
 in contiguous order (see the explanation for better understanding).
"""

def count_stu(arr,pages):
    students=1
    pageStu=0
    for i in range(len(arr)):
        if arr[i]+pageStu <= pages:
            pageStu += arr[i]
        else:
            students += 1
            pageStu = arr[i]
    return students

def findPages(arr, n, m):

    # Write your code here
    # Return the minimum number of pages
    if m > n:
        return -1
    low=max(arr)
    high = sum(arr)
    while low<=high:
        mid = low + (high - low)//2
        students = count_stu(arr,mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low



print(findPages([12,34,67,90],4,2))
"""
Sample Input 1:
4 2
12 34 67 90
Sample Output 1:
113
"""