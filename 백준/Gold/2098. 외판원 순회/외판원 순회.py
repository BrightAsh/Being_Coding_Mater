import sys
input = sys.stdin.read
from functools import lru_cache

data = input().split()
N = int(data[0])
W = [list(map(int, data[i*N+1:(i+1)*N+1])) for i in range(N)]

@lru_cache(None)
def tsp(current, visited):
    if visited == (1 << N) - 1:  # 모든 도시를 방문했으면
        return W[current][0] if W[current][0] > 0 else float('inf')

    min_cost = float('inf')
    for next in range(N):
        if not visited & (1 << next) and W[current][next] != 0:
            cost = tsp(next, visited | (1 << next)) + W[current][next]
            min_cost = min(min_cost, cost)
    return min_cost

print(tsp(0, 1))  # 0번 도시에서 시작, 0번만 방문한 상태
