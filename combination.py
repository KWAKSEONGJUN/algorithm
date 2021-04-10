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

items = [1, 2, 3, 4, 5]
conbination(items, 2, 0, 0)