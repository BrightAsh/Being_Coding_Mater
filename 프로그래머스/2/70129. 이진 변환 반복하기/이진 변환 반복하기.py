

def solution(s):
    cnt,remove = 0,0
    while s != '1':
        remove += len(s) - s.count('1')
        cnt += 1
        s = bin(s.count('1'))[2:]
    return [cnt, remove]
