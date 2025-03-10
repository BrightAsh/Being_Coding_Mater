def solution(answers):
    
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    ss= [0,0,0]
    
    for i,answer in enumerate(answers):
        if answer == s1[i%5]: ss[0]+=1
        if answer == s2[i%8]: ss[1]+=1
        if answer == s3[i%10]: ss[2]+=1
    
    
    return [i+1 for i,s in enumerate(ss) if s == max(ss)]