def calculate_angle(h, m, s):
    hour_angle = (h % 12) * 30 + (m * 0.5) + (s * (0.5 / 60))
    minute_angle = (m * 6) + (s * 0.1)
    second_angle = s * 6
    return hour_angle, minute_angle, second_angle

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    
    for current_time in range(start_time, end_time):
        h, m, s = current_time // 3600, (current_time // 60) % 60, current_time % 60
        hour_angle, minute_angle, second_angle = calculate_angle(h, m, s)
        if second_angle+6 - 0.1 > minute_angle and second_angle <= minute_angle:
            answer+=1
        if second_angle+6 - 1/120 > hour_angle and second_angle <= hour_angle:
            answer+=1
        if hour_angle == minute_angle == second_angle:
            answer-=1
    
    h, m, s = end_time // 3600, (end_time // 60) % 60, end_time % 60
    hour_angle, minute_angle, second_angle = calculate_angle(h, m, s)
    print(h)
    print(m)
    print(s)
    print(hour_angle)
    print(minute_angle)
    print(second_angle)
    if second_angle == minute_angle or second_angle == hour_angle:
        answer+=1

    return answer