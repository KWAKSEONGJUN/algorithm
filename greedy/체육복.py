def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r-1)
        elif r + 1 in _lost:
            _lost.remove(r+1)

    answer = n - len(_lost)
    return answer
    
print(solution(7, [2, 4, 5, 6, 7], [1, 3, 4, 5, 6, 7]))