n=int(input())

val = 3.14*n*n

if( val - int(val) > 0.5):
    print(int(val)+1)
else:
    print(int(val))