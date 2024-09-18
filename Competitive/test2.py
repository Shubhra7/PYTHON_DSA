def win_joshep(n,k):
    winner = 1
    for i in range(2,n+1):
        winner = (winner + (k-1))%i + 1
    # print(winner)
    return winner

print(win_joshep(41,2))