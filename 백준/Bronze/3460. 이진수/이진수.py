def solution(num):
    result=[]
    idx = 0
    while num>0:
        if num % 2 ==1:
            result.append(idx)
        num=num//2
        idx+=1

    return ' '.join(map(str,result))
    
n = int(input())
for num in range(n):
    num = int(input())
    print(solution(num))


