def rebound_height(H,V,Vn):
    ans = H * ((V/Vn)**2)
    return ans


H, V, Vn = map(int,input().split())

print(int(rebound_height(H,V,Vn)))