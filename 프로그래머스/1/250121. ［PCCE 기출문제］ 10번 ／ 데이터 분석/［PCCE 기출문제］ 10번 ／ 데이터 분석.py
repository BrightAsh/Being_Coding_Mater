def solution(data, ext, val_ext, sort_by):

    dic = {'code': 0,'date':1,'maximum':2,'remain':3}
    
    data = sorted(data,key = lambda x: x[dic[ext]])
    
    for i,d in enumerate(data):
        if d[dic[ext]] > val_ext:
            break;
    data = sorted(data[:i], key = lambda x: x[dic[sort_by]])

    return data