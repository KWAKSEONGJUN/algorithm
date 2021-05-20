visited = []
res = []

def conbination(items, r, pos, index):
    if pos == r:
        print(res)
        return
    
    for item in items[index:]:
        if item not in visited:
            res.append(item)
            visited.append(item)
            conbination(items, r, pos+1, items.index(item))
            visited.pop()
            res.pop()


def combination2(arr, r):
    
    # 조합을 저장할 배열
    result = []
    
    # 실제 조합을 구하는 함수
    def combinate(c, index):
        if len(c) == r:
            result.append(c)
            return 
        
        for idx, data in enumerate(arr):
            # 중복되는 조합이 생성되지 않게 마지막으로 들어온 원소의 인덱스보다
            # 새로 추가하는 원소의 인덱스가 큰 경우만 조합을 생성한다.
            if idx > index:
                combinate(c + [data], idx)
    
    combinate([], -1)
    
    return result

for r in combination2(['A', 'B', 'C', 'D'], 2):
    print(r)

items = [1, 2, 3, 4, 5]
conbination(items, 2, 0, 0)