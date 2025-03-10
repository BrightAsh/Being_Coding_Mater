def solution(n, left, right):
    l_n = left//n
    l_r = left%n
    
    r_n = right//n
    r_r = right%n
    result=[]
    for i in range(l_n,r_n+1):
        result.extend([i+1]*(i+1)+[j+1 for j in range(i+1,n)])
    
    return result[l_r:l_r+(right-left)+1]