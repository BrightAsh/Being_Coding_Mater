def solution(n):
    if n==1: return 1
    elif n==2: return 2
    else:
        a = 1
        b = 2
        for _ in range(n-2):
            a,b = b, (a+b) % 1234567
        return b