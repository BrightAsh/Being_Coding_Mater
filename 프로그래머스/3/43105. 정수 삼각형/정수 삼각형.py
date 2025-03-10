def solution(triangle):
    h=len(triangle)
    w=len(triangle[-1])
    
    dp=[[0]* (i+1) for i in range(w)]
    dp[0][0]=triangle[0][0]
    
    for i in range(1,w):
        dp[i][0]=dp[i-1][0]+triangle[i][0]
        dp[i][i]=dp[i-1][i-1]+triangle[i][i]

         
    for i in range(2,w):
        for j in range(1,i):
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    
    
    return max(dp[-1])