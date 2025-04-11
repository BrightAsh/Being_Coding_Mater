s1 = input().strip()
s2 = input().strip()
dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[j][i] = dp[j-1][i-1]+1
        else:
            dp[j][i] = max(dp[j][i-1],dp[j-1][i])
print(dp[-1][-1])
            
            