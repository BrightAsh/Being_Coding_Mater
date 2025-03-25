def solution(brown, yellow):
    brown = (brown - 4) //2
    for b in range(1,brown//2+1):
        if yellow == b * (brown - b):
            return [brown - b + 2, b + 2]
