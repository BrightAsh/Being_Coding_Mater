def a(n,p):
    array = [1,1,0,1,1]
    answer = 0
    while(n>1):
        if p-1 >= 5**n: break;
        index = ((p-1) // 5**(n-1))
        answer += 4**(n-1) * sum(array[index+1:])
        if index == 2: break;
        p = (p-1) % (5 ** (n - 1)) + 1
        n=n-1
    answer += sum(array[p-1:]) 
    return answer

def solution(n, l, r):
    return a(n,l) - a(n,r+1)


    