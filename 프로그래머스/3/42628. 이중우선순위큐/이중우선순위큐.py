import heapq as h

def solution(operations):
    a=[]
    for op in operations:
        if 'I' in op:
            h.heappush(a,int(op.split()[1]))
        elif a:
            if op=='D 1':
                a.remove(max(a))
                h.heapify(a)
            elif op=='D -1':
                h.heappop(a)
    return [max(a),h.heappop(a)] if a else [0,0]