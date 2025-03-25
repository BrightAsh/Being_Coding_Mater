def solution(A,B):
    A = sorted(A,reverse = True)
    B = sorted(B,reverse = False)
    answer = 0
    for a,b in zip(A,B):
        answer += a*b
    return answer