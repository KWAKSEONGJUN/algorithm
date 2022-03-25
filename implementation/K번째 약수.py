
def solution(n, k):
    measure =[i for i in range(1, n+1) if n % i == 0]
    
    if len(measure) >= k:
        return measure[k-1]
    else:
        return -1
                

if __name__ == '__main__':
    n, k = map(int, input().split())
    res = solution(n, k)
    print(res)
    