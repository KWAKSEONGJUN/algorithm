def solution(n, s, e, k):
    sep = sorted(nums[s-1:e])
    return sep[k-1]


if __name__ == '__main__':
    T = int(input())

    for t in range(T):
        n, s, e, k = map(int, input().split())
        nums = list(map(int, input().split()))
        print(solution(n, s, e, k))

    
    

