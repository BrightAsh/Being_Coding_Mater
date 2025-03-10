from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0, -1)]) 
    while q:
        n,idx = q.popleft() 
        r=sum(numbers[idx+1:])
        if idx+1<len(numbers):
            if target - r <= n <= target + r:
                q.append((n+numbers[idx+1],idx+1))
                q.append((n-numbers[idx+1],idx+1))
        else:
            if n==target: 
                answer+=1
    return answer