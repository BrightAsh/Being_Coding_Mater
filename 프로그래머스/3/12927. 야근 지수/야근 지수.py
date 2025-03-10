import heapq as h

def solution(n, works):
    w = [-w for w in works]
    h.heapify(w)
    
    for _ in range(n):
        max_w = h.heappop(w)
        if max_w == 0:
            break
        h.heappush(w,max_w+1)
    return sum(i**2 for i in w)