# First occurance of x2 in x1

def find_first_occurance(x1,x2):
    diff = len(x1) - len(x2)
    for i in range(diff + 1):
        if x1[i:i+len(x2)] == x2:
            return i
    else:
        return -1

x1 = "psadbutsad"
x2 = "sad"

print(find_first_occurance(x1,x2))



