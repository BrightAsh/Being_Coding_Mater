def to_oct(n,w):
    return sum(int(v) * (w ** idx) for idx, v in enumerate(n[::-1]))


def solution(expressions):
    what = list(range(2, 10))
    answer = []
    new_what = []
    

    q=''
    for i in expressions:
        a, e, b, _, c = i.split(' ')
        if 'X' not in i:
            q = q + a + b + c
        elif 'X' in i:
            q = q + a + b  
    for w in what:
        if len(what)==1: break
        if all(int(i) < w for i in q):
            new_what.append(w)
    what=new_what
    

    for i in expressions:
        if 'X' not in i and len(what) > 1:
            a, e, b, _, c = i.split(' ')
            new_what = []
            for w in what:
                a_val = to_oct(a, w)
                b_val = to_oct(b, w)
                c_val = to_oct(c, w)
                if (e == '+' and a_val + b_val == c_val) or (e == '-' and a_val - b_val == c_val):
                    new_what.append(w)
            what = new_what
    for i in expressions:
        if 'X' in i:
            a, e, b, _, _ = i.split(' ')
            eq = []
            for w in what:
                if e == '+':  
                    result = to_oct(a, w) + to_oct(b, w)
                elif e == '-':
                    result = to_oct(a, w) - to_oct(b, w)
                to_result = ''
                while result > 0:
                    to_result = str(result % w) + to_result
                    result //= w
                if to_result == '':
                    to_result = '0'
                eq.append(int(to_result))
                
            if len(set(eq)) == 1:
                answer.append(f'{a} {e} {b} = {eq[0]}')
            else:
                answer.append(f'{a} {e} {b} = ?')

    return answer