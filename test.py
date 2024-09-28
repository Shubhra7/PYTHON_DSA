text1 = 'adventure'
text2 = 'future'

lt1, lt2 =len(text1), len(text2)

dp = [ [0 for i in range(lt1+1)] for j in range(lt2+1)]
print(dp)
