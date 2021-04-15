def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    for v1, v2 in edges:
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    visited = [False] * len(a)
    answer = dfs(tree, 0, visited, a)
    
    if sum(a) != 0:
        return -1

    return answer

def dfs(tree, start, visited, a):
    visited[start] = True
    
    cnt = 0
    for t in tree[start]:
        if not visited[t]:
            cnt += dfs(tree, t, visited, a)
            
            a[start] += a[t]
            cnt += a[t]
            a[t] = 0

    return cnt

print(solution([-5,0,3,1,1], [[1,0],[1,3],[3,2],[3,4]]))
print(solution([0,1,0], [[0,1],[1,2]]))