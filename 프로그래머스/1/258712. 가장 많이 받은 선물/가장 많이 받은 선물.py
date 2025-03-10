
def solution(friends, gifts):
    tmp = 0
    
    gift_num = {name: {'giv': 0, 'rec': 0} for name in friends}
    
    for gift in gifts:
        giv, rec = gift.split()
        gift_num[giv]['giv'] += 1
        gift_num[rec]['rec'] += 1
    
    for friend in gift_num:
        gift_num[friend]['num'] = gift_num[friend]['giv'] - gift_num[friend]['rec']
    
    
    for i,target in enumerate(friends):
        next_sum = 0
        gift_list = {name: {'giv': 0, 'rec': 0} for name in friends}  
        for j,gift in enumerate(gifts):
            if target == gift.split()[0]:
                gift_list[gift.split()[1]]['giv'] +=1     
            if target == gift.split()[1]:       
                gift_list[gift.split()[0]]['rec'] +=1
                
        for compare in gift_list:
            if compare == target:
                continue;
            if gift_list[compare]['giv'] > gift_list[compare]['rec']:
                next_sum +=1
            elif gift_list[compare]['giv'] == gift_list[compare]['rec']:
                if gift_num[target]['num'] > gift_num[compare]['num']:
                    next_sum +=1
        if next_sum > tmp:
            tmp = next_sum


    return tmp