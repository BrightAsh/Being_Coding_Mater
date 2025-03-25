def solution(s):
    s=list(s)
    tmp = True
    for i,v in enumerate(s):
        if tmp and v != ' ':
            s[i] = s[i].upper()
            tmp = 0
        elif v == ' ':
            tmp = 1
        else:
            s[i] = s[i].lower()
        
    return ''.join(s)

print(solution("asd eaew    eawkfla"))