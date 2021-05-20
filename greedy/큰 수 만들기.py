def solution(number, k):
    n = len(number) - k
    res = []
    start = 0
    for i in range(k, len(number)):
        mx = max(number[start:i+1])
        start = number.index(mx, start, i+1) + 1
        res.append(mx)
    
    return ''.join(res)
        
solution("4177252841", 4)
        
        
        
            
        
            
    