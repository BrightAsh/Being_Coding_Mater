from collections import deque, defaultdict

def bfs_search(roads, destination, n):
    # 그래프 생성
    g = defaultdict(list)
    for a, b in roads:
        g[a].append(b)
        g[b].append(a)

    # BFS 초기화
    queue = deque([destination])
    distances = [-1] * (n + 1)  # 방문하지 않은 경우 -1
    distances[destination] = 0  # 목적지는 자기 자신이므로 거리 0

    # BFS 실행
    while queue:
        node = queue.popleft()
        for neighbor in g[node]:
            if distances[neighbor] == -1:  # 방문하지 않은 경우만 추가
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances

def solution(n, roads, sources, destination):
    distances = bfs_search(roads, destination, n)  # 모든 노드의 최단 거리 계산
    return [distances[s] for s in sources]  # sources의 결과를 O(1)로 조회
