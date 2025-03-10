def solution(today, terms, privacies):
    answer = []
    dic = {term.split()[0]:term.split()[1] for term in terms}
    
    for i, privacy in enumerate(privacies):
        d = int(privacy.split()[0].split('.')[2])
        m = int(privacy.split()[0].split('.')[1]) + int(dic[privacy.split()[1]])
        y = int(privacy.split()[0].split('.')[0])
        
        if m > 12:
            y += m //12 if (m % 12) != 0 else m //12 -1
            m = m % 12 if (m % 12) != 0 else 12

        p = f"{y:04d}.{m:02d}.{d:02d}"
        
        if today >= p:
            answer.append(i+1)

    return answer