def solution(new_id):
    new_id = new_id.lower()
    
    valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = ''.join(ch for ch in new_id if ch in valid_chars)
    
    tmp = 0
    cid = ""
    for i in new_id:
        if i == '.':
            tmp +=1
        else:
            tmp = 0
        if tmp <= 1:
            cid +=i
    
    while cid.startswith('.'):
        cid = cid[1:]
    while cid.endswith('.'):
        cid = cid[:-1]
    
    if cid == "":
        cid += 'a'
    
    if len(cid) >= 16:
        cid = cid[:15]
    while cid.endswith('.'):
        cid = cid[:-1]
    
    while len(cid) <= 2:
        cid += cid[-1]

    return cid