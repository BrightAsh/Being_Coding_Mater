from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    l = len(begin)
    q = deque([(begin,0)])
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            return cnt
        for w in words:
            if sum([1 for i in range(l) if word[i]==w[i]]) == (l-1):
                q.append((w,cnt+1))
    return cnt

