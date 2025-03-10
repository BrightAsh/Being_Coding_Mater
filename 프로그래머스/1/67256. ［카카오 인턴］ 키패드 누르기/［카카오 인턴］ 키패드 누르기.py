def solution(numbers, hand):
    answer = ""
    L_pos = [3,0]
    R_pos = [3,2]
    
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            L_pos[0] = number // 3
            L_pos[1] = 0
        elif number in [3,6,9]:
            answer += 'R'
            R_pos[0] = number // 3 - 1
            R_pos[1] = 2
        elif number in [2,5,8,0]:
            if number == 0: number = 11
            L_d = abs((number // 3) - L_pos[0]) + abs(1 -L_pos[1])
            R_d = abs((number // 3) - R_pos[0]) + abs(1 -R_pos[1])
            if L_d > R_d or (L_d == R_d and hand =='right') :
                answer += 'R'
                R_pos[0] = number // 3
                R_pos[1] = 1
            elif L_d < R_d or (L_d == R_d and hand =='left')  :
                answer += 'L'
                L_pos[0] = number // 3
                L_pos[1] = 1
                
    return answer