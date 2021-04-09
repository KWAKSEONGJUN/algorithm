not_self = []

for i in range(1, 10001):
    num = i + sum(list(map(int, list(str(i)))))
    not_self.append(num)

for i in range(1, 10001):
    if i not in not_self:
        print(i)