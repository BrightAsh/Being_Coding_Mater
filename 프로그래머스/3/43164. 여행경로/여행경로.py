def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    answer = []
    visited = [False] * len(tickets)
    def dfs(path, depth):
        if depth == len(tickets):
            answer.append(path)
            return True
        
        last = path[-1]
        
        for i, (src, dest) in enumerate(tickets):
            if src == last and not visited[i]:
                visited[i] = True
                dfs(path + [dest], depth + 1)
                visited[i] = False
    
    dfs(["ICN"], 0)
    return answer[0]
