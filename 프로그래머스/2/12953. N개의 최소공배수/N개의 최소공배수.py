from math import gcd


def solution(arr):
    while len(arr)!=1:
        arr = [arr[0]*arr[1]//gcd(arr[0],arr[1])] + arr[2:]
    return arr[0]