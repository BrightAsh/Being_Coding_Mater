import math
def solution(n, stations, w):
    answer = 0
    if len(stations)>1:
        for i in range(len(stations[:-1])):
            answer+=math.ceil((stations[i+1] - stations[i]-1-w*2)/(w*2+1))
    answer+=math.ceil((stations[0]-1-w)/(w*2+1)) if stations[0]-1-w > 0 else 0
    answer+=math.ceil((n - stations[-1]-w)/(w*2+1))  if n - stations[-1]-w >0 else 0
    return answer