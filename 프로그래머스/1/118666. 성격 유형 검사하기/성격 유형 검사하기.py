def solution(survey, choices):
    kind = ['R','T','C','F','J','M','A','N']
    dic = {a:0 for a in kind}
    answer = ''
    
    for i in range(len(choices)):
        if choices[i] <4:
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] >4:
            dic[survey[i][1]] += choices[i] - 4
    
    for i in range(4):
        if dic[kind[i*2]] > dic[kind[i*2+1]]:
            answer += kind[i*2]
        elif dic[kind[i*2]] < dic[kind[i*2+1]]:
            answer += kind[i*2+1]
        elif dic[kind[i*2]] == dic[kind[i*2+1]]:
            answer += sorted([kind[i*2],kind[i*2+1]])[0]
            print( sorted([kind[i*2],kind[i*2+1]]))
    return answer