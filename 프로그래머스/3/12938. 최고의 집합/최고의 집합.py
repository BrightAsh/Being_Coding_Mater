def solution(n, s):
    a = s%n
    b = s//n
    if (b+1)**a*(b)**(n-a)!=0:
        return [b]*(n-a)+[b+1]*a
    else:
        return [-1]