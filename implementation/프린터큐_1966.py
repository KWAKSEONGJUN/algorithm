t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importances = list(map(int, input().split()))
    documents = [i for i in range(n)]

    printout, res = -1, 0
    mx = max(importances)
    while printout != m: 
        front = importances.pop(0)
        document = documents.pop(0)

        if front < mx:
            importances.append(front)
            documents.append(document)
        else:
            printout = document
            res += 1

            if importances:
                mx = max(importances)
            
    print(res)


# from collections import deque

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     importances = deque(map(int, input().split()))
#     documents = deque([i for i in range(n)])

#     mx = max(importances)
#     printout, res = -1, 0
#     while printout != m:
#         front = importances.popleft()
#         document = documents.popleft()

#         if front < mx:
#             importances.append(front)
#             documents.append(document)
#         else:
#             printout = document
#             res += 1

#             if importances:
#                 mx = max(importances)
#     print(res)
