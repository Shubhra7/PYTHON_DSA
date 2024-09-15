stone=input()
instruction=input()

idx=0
for i in range(len(instruction)):
    if (instruction[i] == stone[idx]):
        idx += 1

print(idx+1)