def solution(park, routes):
    for i, p in enumerate(park):
        pos = p.find("S")
        if pos != -1:
            break;

    dx,dy = [pos,pos],[i,i]
    x_limit, y_limit = len(park[0]),len(park)
    
    for r in routes:
        d,n = r.split()
        if d == "E": dx[1] = dx[0] + int(n)
        elif d=="S": dy[1] = dy[0] + int(n)
        elif d =="W": dx[1] = dx[0] - int(n)
        elif d =="N": dy[1] = dy[0] - int(n)
        
        if dx[1] >= x_limit or dy[1] >= y_limit or dx[1] < 0 or dy[1] <0:
            dx[1], dy[1] = dx[0], dy[0]
            continue;
        
        if dy[0] == dy[1]:
            s = min(dx)
            e = max(dx) + 1
            if "X" in park[dy[0]][s:e]:
                dx[1] = dx[0]
                continue;
            dx[0] = dx[1]
            
        elif dx[0] == dx[1]:
            s = min(dy)
            e = max(dy) + 1
            p_array = [park[s+i][dx[0]] for i in range(e-s)]
            if "X" in p_array:
                dy[1] = dy[0] 
                continue;
            dy[0] = dy[1]  
        
    return [dy[0],dx[0]]