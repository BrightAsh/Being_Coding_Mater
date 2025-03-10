def solution(name, yearning, photo):
    answer = []
    dic ={name[i]:yearning[i] for i in range(len(name))}
    
    for name_list in photo:
        suma = 0
        for name in name_list:
            try:
                suma += dic[name]
            except KeyError:
                continue;
        answer.append(suma)
    return answer