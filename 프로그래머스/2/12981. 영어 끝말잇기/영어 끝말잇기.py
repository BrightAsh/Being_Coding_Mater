def solution(n, words):
    tmp = words[0][-1]
    l = [words[0]]
    for i,v in enumerate(words[1:]):
        if v in l or v[0] != tmp:
            return [(i+1)%n+1,(i+1)//n+1]
        tmp = v[-1]
        l.append(v)
    return [0,0]