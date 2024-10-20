def second_lar_count(arr):
    dem = sorted(set(arr),reverse=True)
    return arr.count(dem[1])


arr = [1,2,3,3,4,4]
print(second_lar_count(arr))