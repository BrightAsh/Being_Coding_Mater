def solution(genres, plays):
    g = list(set(genres))
    
    dict={ i:[] for i in g}
    
    
    for i in range(len(plays)):
        dict[genres[i]].append((plays[i], i))
    
    for genre in dict:
        dict[genre] = sorted(dict[genre], key=lambda x: -x[0])
    
    s = sorted(dict.keys(), key=lambda x: sum([play[0] for play in dict[x]]), reverse=True)
    
    
    answer = []
    for genre in s:
        answer.extend([play[1] for play in dict[genre][:2]])

    return answer
    
