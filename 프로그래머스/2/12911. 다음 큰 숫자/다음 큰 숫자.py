def solution(n):
    n_1 = str(bin(n)[2:]).count('1')
    i = 1
    for _ in range(10):
        if n_1 == str(bin(n+i)[2:]).count('1'):
            return n+i
        i +=1