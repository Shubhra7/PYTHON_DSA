# https://www.naukri.com/code360/problems/next-greater-element_920451
# Striver stacka and queue video

"""
Problem statement
You have been given an array/list ‘ARR’ consisting of ‘N’ positive integers. Your task is to return the Next Greater Element(NGE) for every element.

The Next Greater Element for an element ‘X’ is the first element on the right side of ‘X’ in the array 'ARR', which is greater than ‘X’. If no such element exists to the right of ‘X’, then return -1.

For example:
For the given array 'ARR' = [7, 12, 1, 20]

The next greater element for 7 is 12.
The next greater element for 12 is 20. 
The next greater element for 1 is 20. 
There is no greater element for 20 on the right side.

So, the output is [12, 20, 20, -1].
"""

def nextGreaterElement(arr, n):
	# Write your code here.
	stack=[]
	res=[0 for _ in range(n)]
	for i in range(len(arr)-1,-1,-1):
		while stack and stack[-1]<=arr[i]:
			stack.pop()
		if stack:
			res[i]=stack[-1]
		else:
			res[i]=-1
		stack.append(arr[i])
	return res
arr=[7, 12, 1, 20]
print(nextGreaterElement(arr,len(arr)))