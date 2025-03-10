def distance(s,e,m,n,cond):
    d=[
        (-s[0]-e[0])**2 + (s[1]-e[1])**2, 
        (s[0]-e[0])**2 + (-s[1]-e[1])**2,
        (2*m-s[0]-e[0])**2 + (s[1]-e[1])**2,
        (s[0]-e[0])**2 + (2*n-s[1]-e[1])**2,
        (-s[0]-e[0])**2 + (-s[1]-e[1])**2,
        (-s[0]-e[0])**2 + (2*n-s[1]-e[1])**2,
        (2*m-s[0]-e[0])**2 + (-s[1]-e[1])**2,
        (2*m-s[0]-e[0])**2 + (2*n-s[1]-e[1])**2
        
    ]
    if cond is not None:
        d[cond] = max(d)+1 
    return d

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        start_pos = [startX,startY]
        if start_pos[1]==ball[1]: 
            if start_pos[0]>ball[0]:
                answer.append(min(distance(start_pos,ball,m,n,0)))
            else:
                answer.append(min(distance(start_pos,ball,m,n,2)))

        elif start_pos[0]==ball[0]: 
            if start_pos[1]>ball[1]:
                answer.append(min(distance(start_pos,ball,m,n,1)))
            else:
                answer.append(min(distance(start_pos,ball,m,n,3))) 
        else: 
            answer.append(min(distance(start_pos,ball,m,n,None)))
              
    return answer


