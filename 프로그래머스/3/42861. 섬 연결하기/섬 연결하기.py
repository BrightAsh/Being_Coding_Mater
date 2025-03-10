# Union-Find: 부모 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# Union-Find: 두 집합을 합치기
def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def solution(n, costs):
    # 비용 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    
    # Union-Find 초기화
    parent = [i for i in range(n)]
    rank = [0] * n
    
    total_cost = 0
    edge_count = 0
    
    for u, v, cost in costs:
        # 두 섬이 같은 집합에 속하지 않는다면 연결
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += cost
            edge_count += 1
            
            # MST가 완성되면 종료
            if edge_count == n - 1:
                break
    
    return total_cost
