from collections import Counter
c = Counter(input())
odd = 0
for k,v in sorted(c.items()):
    if v%2==1:
        odd+=1
        m = k
if odd <=1 :
    answer = ''
    for k,v in sorted(c.items()):
        answer = answer + (k*(v//2))
    print(answer + (m if odd else '') +answer[::-1] )
else:
    print("I'm Sorry Hansoo")