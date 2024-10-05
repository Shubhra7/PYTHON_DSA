import copy

old_list = [[1,2],[3,4],[5,6,7]]
new_list = copy.deepcopy(old_list)   # for deep copy "deepcopy" used 

# If append something 
old_list.append([9,9,9,9,9])

print("After appending: ")
print(old_list)
print(new_list)
print()

# If make some changes in existing things

old_list[1][1] = 69

print("After making changes in existing list : ")
print(old_list)
print(new_list)
print("In deep copy both are not changed!!!")

