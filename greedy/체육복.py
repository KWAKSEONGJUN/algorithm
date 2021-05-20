def solution(n, lost, reserve):
    reserve2 = [i for i in reserve if i not in lost]
    lost2 = [i for i in lost if i not in reserve]
    
    for r in reserve2:
        front, back = r - 1, r + 1
        if front in lost2:
            lost2.remove(front)
        elif back in lost2:
            lost2.remove(back)
            
    return n - len(lost2)
    
    
print(solution(3, [3], [1]))
