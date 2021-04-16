import sys
sys.setrecursionlimit(1000000)

answer = 0

def dfs(tree, a, start, visited):
    global answer
    visited[start] = True
   
    for next_node in tree[start]:
        if not visited[next_node]:
            tmp = dfs(tree, a, next_node, visited)
            answer += abs(tmp)
            a[start] += tmp
        
    return a[start]

def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    tree = [[] for _ in range(len(a))]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    visited = [False] * len(a)
    dfs(tree, a, 0, visited)

    return answer


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))


# 0 1 3
# 1 0 
# 2 3
# 3 0 2 4
# 4 3