from collections import Counter
def second_lar_count(arr):
    l = sorted(set(arr))
    if(len(l) < 2):
        return 0
    d = Counter(arr)
    print(d[l[-2]])
    return l[-2]

arr = [1,2,5,5,5,6,3,3,4,4]
print(second_lar_count(arr))

arr1 = [2,2,2,2,2]
print(second_lar_count(arr1))