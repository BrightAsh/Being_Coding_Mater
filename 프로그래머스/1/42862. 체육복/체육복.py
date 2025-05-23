def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost) 
    _lost = set(lost) - set(reserve)  

    answer = n - len(_lost) 
    
    for l in sorted(_lost): 
        if l - 1 in _reserve:
            _reserve.remove(l - 1)
            answer += 1
        elif l + 1 in _reserve:
            _reserve.remove(l + 1)
            answer += 1
            
    return answer
